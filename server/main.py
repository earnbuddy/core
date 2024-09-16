import json
import os
from contextlib import asynccontextmanager
from datetime import datetime
from typing import Dict, Any, AsyncGenerator


from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, WebSocket, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import func
from sqlmodel import Session, select
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocketDisconnect
from tortoise import generate_config, Tortoise
from tortoise.contrib.fastapi import RegisterTortoise
from database import init_db

from models import Client, EarnerHeartBeat, Earner, HeartbeatData
from tasks.HoneyGainTask import HoneyGainTask

@asynccontextmanager
async def lifespan_test(app: FastAPI) -> AsyncGenerator[None, None]:
    config = generate_config(
        os.getenv("TORTOISE_TEST_DB", "sqlite://db.sqlite3"),
        app_modules={"models": ["models"]},
        testing=True,
        connection_label="models",
    )
    async with RegisterTortoise(
        app=app,
        config=config,
        generate_schemas=True,
        add_exception_handlers=True,
        _create_db=True,
    ):
        # db connected
        yield
        # app teardown
    # db connections closed
    await Tortoise._drop_databases()


def register_orm(app):
    pass


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    if getattr(app.state, "testing", None):
        async with lifespan_test(app) as _:
            yield
    else:
        # app startup
        async with register_orm(app):
            # db connected
            yield
            # app teardown
        # db connections closed

app = FastAPI()

AUTH_USERNAME = os.getenv("AUTH_USERNAME", default="admin")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD", default="admin")

# Initialize HTTP Basic Authentication
security = HTTPBasic()


def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != AUTH_USERNAME or credentials.password != AUTH_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )


# add cors allow all
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/clients/", response_model=list[Client])
def read_clients(credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    with Session(engine) as session:
        clients = session.exec(select(Client)).all()
    return clients


@app.delete("/api/clients/{client_name}/")
def delete_client(client_name: str, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    with Session(engine) as session:
        client = session.get(Client, client_name)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        session.delete(client)
        session.commit()
    return {"message": "Client deleted"}

@app.post("/api/clients/{client_name}/heartbeat/")
async def handle_heartbeat(client_name: str, heartbeat_data: HeartbeatData,
                           credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    with Session(engine) as session:
        # check if client exists
        # if not, create new client with id and the heartbeat data
        # if it exists, update the heartbeat data only
        client = session.exec(select(Client).filter(Client.device_name == client_name)).first()

        if not client:
            client = Client()
            client.device_name = client_name
            client.last_ping = datetime.now()
            client.client_version = heartbeat_data.client_version
            client.public_ip = heartbeat_data.public_ip
            client.docker_version = heartbeat_data.docker_version
            client.system_platform = heartbeat_data.system_platform
            session.add(client)
            session.commit()
            session.refresh(client)
        else:
            client.last_ping = datetime.now()
            client.client_version = heartbeat_data.client_version
            client.public_ip = heartbeat_data.public_ip
            client.docker_version = heartbeat_data.docker_version
            client.system_platform = heartbeat_data.system_platform
            session.commit()
            session.refresh(client)

    return client


@app.websocket("/api/clients/{client_name}/ws")
async def websocket_endpoint(client_name: str, websocket: WebSocket,
                             credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    await websocket.accept()
    clients_ws.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket)


@app.post("/api/earners/{earner_id}/settings/")
async def handle_earner_settings(earner_id: str, settings: Dict[str, Any],
                                 credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    with Session(engine) as session:
        earner = session.get(Earner, earner_id)
        if not earner:
            earner = Earner(id=earner_id, settings=settings)
            session.add(earner)
            session.commit()
            session.refresh(earner)
        else:
            earner.settings = settings
            session.commit()
            session.refresh(earner)
    return earner


@app.get("/api/earners/{earner_id}/settings/")
def read_earner_settings(earner_id: str, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    with Session(engine) as session:
        earner = session.get(Earner, earner_id)
        if not earner:
            raise HTTPException(status_code=404, detail="Earner not found")
    return earner


@app.get("/api/earners/settings/")
def read_earners(credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    with Session(engine) as session:
        earners = session.exec(select(Earner)).all()
    return earners


@app.post("/api/clients/{client_name}/{earner_id}/heartbeat/")
async def handle_earner_heartbeat(client_name: str, earner_id: str, heartbeat_data: EarnerHeartBeat,
                                  credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    with Session(engine) as session:
        earner_heartbeat = EarnerHeartBeat(
            from_client_id=client_name,
            from_earner=earner_id,
            cpu_usage=heartbeat_data.cpu_usage,
            ram_usage=heartbeat_data.ram_usage,
            uptime=heartbeat_data.uptime,
            extra_data=heartbeat_data.extra_data,
            created_at=datetime.now().isoformat()
        )
        session.add(earner_heartbeat)
        session.commit()
        session.refresh(earner_heartbeat)

    return earner_heartbeat


@app.get("/api/clients/{client_name}/earners/")
def read_client_earners(client_name: str, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    with Session(engine) as session:
        subquery = (
            select(
                EarnerHeartBeat.from_earner,
                func.max(EarnerHeartBeat.created_at).label("latest_heartbeat")
            )
            .filter(EarnerHeartBeat.from_client_id == client_name)
            .group_by(EarnerHeartBeat.from_earner)
            .subquery()
        )

        earners = (
            session.exec(
                select(EarnerHeartBeat)
                .join(subquery, (EarnerHeartBeat.from_earner == subquery.c.from_earner) & (
                        EarnerHeartBeat.created_at == subquery.c.latest_heartbeat))
            )
            .all()
        )
    return earners


@app.get("/api/earners/{earner_id}/heartbeats/")
def read_earner_heartbeats(earner_id: str, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    with Session(engine) as session:
        subquery = (
            select(
                EarnerHeartBeat.from_client_id,
                func.max(EarnerHeartBeat.created_at).label("latest_heartbeat")
            )
            .filter(EarnerHeartBeat.from_earner == earner_id)
            .group_by(EarnerHeartBeat.from_client_id)
            .subquery()
        )

        heartbeats = (
            session.exec(
                select(EarnerHeartBeat)
                .join(subquery, (EarnerHeartBeat.from_client_id == subquery.c.from_client_id) &
                      (EarnerHeartBeat.created_at == subquery.c.latest_heartbeat))
            )
            .all()
        )
    return heartbeats


@app.on_event("startup")
@repeat_at(cron="*/1 * * * *") #every 2nd minute
def run_tasks():
    print("Running tasks")
    HoneyGainTask().run()


app.mount("/", StaticFiles(directory="public", html=True), name="static")


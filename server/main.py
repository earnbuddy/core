import json
from datetime import datetime
from typing import Dict, Any

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, WebSocket, HTTPException
from sqlalchemy import func
from sqlmodel import  Session, select
from starlette.staticfiles import StaticFiles
from starlette.websockets import WebSocketDisconnect

from database import create_db_and_tables, engine
from models import Client, EarnerHeartBeat, Earner, HeartbeatData

# An array of all clients used for the websocket
clients = []

clients_ws = []
app_ws = []

app = FastAPI()

# add cors allow all
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/clients/", response_model=list[Client])
def read_clients():
    with Session(engine) as session:
        clients = session.exec(select(Client)).all()
    return clients

@app.post("/api/clients/{client_name}/heartbeat/")
async def handle_heartbeat(client_name: str, heartbeat_data: HeartbeatData):
    print(client_name)
    with Session(engine) as session:
        # check if client exists
        # if not, create new client with id and the heartbeat data
        # if it exists, update the heartbeat data only
        client = session.exec(select(Client).filter(Client.device_name == client_name)).first()

        if not client:
            print("Creating new client")
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
            print("Updating existing client")
            client.last_ping = datetime.now()
            client.client_version = heartbeat_data.client_version
            client.public_ip = heartbeat_data.public_ip
            client.docker_version = heartbeat_data.docker_version
            client.system_platform = heartbeat_data.system_platform
            session.commit()
            session.refresh(client)

    return client


@app.websocket("/api/clients/{client_name}/ws")
async def websocket_endpoint(client_name: str, websocket: WebSocket):
    await websocket.accept()
    clients_ws.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket)

@app.post("/api/earners/{earner_id}/settings/")
async def handle_earner_settings(earner_id: str, settings: Dict[str, Any]):
    print(earner_id)
    print(settings)

    with Session(engine) as session:
        earner = session.get(Earner, earner_id)
        if not earner:
            print("Creating new earner")
            earner = Earner(id=earner_id, settings=settings)
            session.add(earner)
            session.commit()
            session.refresh(earner)
        else:
            print("Updating existing earner")
            earner.settings = settings
            session.commit()
            session.refresh(earner)
    return earner

@app.get("/api/earners/{earner_id}/settings/")
def read_earner_settings(earner_id: str):
    with Session(engine) as session:
        earner = session.get(Earner, earner_id)
        if not earner:
            raise HTTPException(status_code=404, detail="Earner not found")
    return earner

@app.get("/api/earners/settings")
def read_earners():
    with Session(engine) as session:
        earners = session.exec(select(Earner)).all()
    return earners

@app.post("/api/clients/{client_name}/{earner_id}/heartbeat/")
async def handle_earner_heartbeat(client_name: str, earner_id: str, heartbeat_data: EarnerHeartBeat):
    print(client_name)
    print(earner_id)
    print(heartbeat_data)

    with Session(engine) as session:
        earner_heartbeat = EarnerHeartBeat(
            from_client_id=client_name,
            from_earner=earner_id,
            cpu_usage=heartbeat_data.cpu_usage,
            ram_usage=heartbeat_data.ram_usage,
            uptime=heartbeat_data.uptime,
            # extra_data=heartbeat_data.extra,
            created_at=datetime.now().isoformat()
        )
        session.add(earner_heartbeat)
        session.commit()
        session.refresh(earner_heartbeat)

    return earner_heartbeat


@app.get("/api/clients/{client_name}/earners/")
def read_client_earners(client_name: str):
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
                .join(subquery, (EarnerHeartBeat.from_earner == subquery.c.from_earner) & (EarnerHeartBeat.created_at == subquery.c.latest_heartbeat))
            )
            .all()
        )
    return earners

app.mount("/", StaticFiles(directory="public", html=True), name="static")
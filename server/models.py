from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, SQLModel, JSON, Relationship
from sqlalchemy import Column


class BaseClient(SQLModel):
    device_name: str | None
    last_ping: datetime
    client_version: Optional[str]
    public_ip: Optional[str]
    docker_version: Optional[str]
    system_platform: Optional[str]
    created_at: Optional[str] = Field(default=None)


class Client(BaseClient, table=True):
    id: int = Field(primary_key=True)


class ClientHeartUsageBase(SQLModel):
    from_client_id: str | None = Field(foreign_key="client.device_name")
    cpu_usage: Optional[float]
    ram_usage: Optional[float]


class ClientHeartUsage(ClientHeartUsageBase, table=True):
    id: str = Field(primary_key=True, unique=True, index=True)


class HeartbeatData(BaseModel):
    device_name: str
    public_ip: Optional[str]
    client_version: Optional[str]
    docker_version: Optional[str]
    system_platform: Optional[str]


class EarnerHeartBeatBase(SQLModel):
    from_client_id: str = Field(foreign_key="client.device_name")
    from_earner: str

    cpu_usage: Optional[float]
    ram_usage: Optional[float]
    uptime: Optional[str]

    extra_data: Optional[dict] = Field(default_factory=dict, sa_column=Column(JSON))

    created_at: Optional[str] = Field(default=None)

class EarnerHeartBeat(EarnerHeartBeatBase, table=True):
    id: int | None = Field(primary_key=True)

class Earner(SQLModel, table=True):
    id: str = Field(primary_key=True)
    settings: Optional[dict] = Field(default_factory=dict, sa_column=Column(JSON))

    created_at: Optional[str] = Field(default=None)
    updated_at: Optional[str] = Field(default=None)

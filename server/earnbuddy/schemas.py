from datetime import datetime

from ninja import Schema, ModelSchema

from earnbuddy.models import Machine, MachineHeartBeat, EarnerHeartBeat, Earner


class MachineOutSchema(Schema):
    name: str
    created_at: datetime
    active: bool

    docker_version: str
    client_version: str
    system_platform: str
    public_ip: str


class MachineHeartBeatInSchema(ModelSchema):
    class Meta:
        model = MachineHeartBeat
        exclude = ['created_at', 'machine']

class EarnerHeartBeatInSchema(ModelSchema):
    class Meta:
        model = EarnerHeartBeat
        exclude = ['created_at', 'machine', 'earner']

class EarnerHeartBeatOutSchema(ModelSchema):
    class Meta:
        model = EarnerHeartBeat
        fields = '__all__'

class EanerSettingsOutSchema(ModelSchema):
    class Meta:
        model = Earner
        fields = ['name', 'settings']
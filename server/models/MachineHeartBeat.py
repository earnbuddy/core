from tortoise.models import Model
from tortoise import fields

class MachineHeartBeat():
    id = fields.IntField(pk=True)
    from_machine = fields.ForeignKeyField("models.Machine", related_name="heartbeats")
    created_at = fields.DatetimeField(auto_now_add=True)
    client_version = fields.CharField(max_length=255)
    docker_version = fields.CharField(max_length=255)
    system_platform = fields.CharField(max_length=255)
    public_ip = fields.CharField(max_length=255)

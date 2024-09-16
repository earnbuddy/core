from tortoise.models import Model
from tortoise import fields

class EarnerHeartBeat(Model):
    id = fields.IntField(pk=True)
    from_earner = fields.ForeignKeyField("models.Earner", related_name="heartbeats")
    from_machine = fields.ForeignKeyField("models.Machine", related_name="heartbeats")
    created_at = fields.DatetimeField(auto_now_add=True)
    extra_data = fields.JSONField()

    def __str__(self):
        return f"{self.from_earner} - {self.from_machine} - {self.created_at}"
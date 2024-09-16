from tortoise.models import Model
from tortoise import fields

class EarnerStats(Model):
    id = fields.IntField(pk=True)
    from_earner = fields.ForeignKeyField("models.Earner", related_name="stats")
    created_at = fields.DatetimeField(auto_now_add=True)
    current_balans = fields.FloatField()
    total_earned = fields.FloatField()
    currency = fields.CharField(max_length=5)


    def __str__(self):
        return f"{self.from_earner} - {self.created_at}"

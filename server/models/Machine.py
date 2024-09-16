from tortoise.models import Model
from tortoise import fields

class Machine(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, unique=True)

    def client_version(self):
        return self.heartbeats[-1].client_version

    def docker_version(self):
        return self.heartbeats[-1].docker_version

    def system_platform(self):
        return self.hearbeats[-1].system_platform

    def public_ip(self):
        return self.hearbeats[-1].public_ip

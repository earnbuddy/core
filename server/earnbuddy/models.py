from symtable import Class

from django.db import models

# Create your models here.
class Earner(models.Model):
    name = models.CharField(primary_key=True, max_length=255, unique=True)
    settings = models.JSONField(default={})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(primary_key=True, max_length=128, unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def public_ip(self):
        return self.heartbeats.last().public_ip

    @property
    def last_heartbeat(self):
        return self.heartbeats.last().created_at

    @property
    def docker_version(self):
        return self.heartbeats.last().docker_version

    @property
    def client_version(self):
        return self.heartbeats.last().client_version

    @property
    def system_platform(self):
        return self.heartbeats.last().system_platform

    def __str__(self):
        return self.name

class MachineHeartBeat(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='heartbeats')
    docker_version = models.CharField(max_length=128)
    client_version = models.CharField(max_length=128)
    public_ip = models.CharField(max_length=128)
    system_platform = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.machine.name

class EarnerHeartBeat(models.Model):
    earner = models.ForeignKey(Earner, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    extra_data = models.JSONField(null=True, blank=True)
    cpu_usage = models.FloatField(null=True)
    memory_usage = models.FloatField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.earner.name
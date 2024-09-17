from typing import List

from django.db.models import Max
from ninja import NinjaAPI

from earnbuddy.models import Machine, MachineHeartBeat, Earner, EarnerHeartBeat
from earnbuddy.schemas import MachineHeartBeatInSchema, MachineOutSchema, EarnerHeartBeatInSchema, \
    EarnerHeartBeatOutSchema, EanerSettingsOutSchema

api = NinjaAPI()

@api.get("/earners/settings/", response=List[EanerSettingsOutSchema])
def list_earners_settings(request):
    return Earner.objects.all()

@api.post("/earners/{earner_name}/settings/")
def save_earner_settings(request, earner_name: str, payload: EanerSettingsOutSchema):
    earner = Earner.objects.get_or_create(name=earner_name)[0]
    earner.settings = payload.dict()
    earner.save()
    return {"message": "received"}

@api.get("/machines/", response=List[MachineOutSchema])
def list_machines(request):
    return Machine.objects.all()


@api.get("/machines/{machine_id}/")
def get_machine(request, machine_id: int):
    return Machine.objects.get(id=machine_id)


@api.post("/machines/{machine_name}/heartbeat/")
def machine_heartbeat(request, machine_name: str, payload: MachineHeartBeatInSchema):
    machine = Machine.objects.get_or_create(name=machine_name)[0]
    MachineHeartBeat.objects.create(**payload.dict(), machine=machine)
    return {"message": "received"}


@api.get("/machines/{machine_name}/earners/", response=List[EarnerHeartBeatOutSchema])
def list_earners(request, machine_name: str):
    latest_heartbeats = EarnerHeartBeat.objects.filter(machine__name=machine_name).values('earner').annotate(
        latest_heartbeat=Max('created_at'))
    return EarnerHeartBeat.objects.filter(created_at__in=[entry['latest_heartbeat'] for entry in latest_heartbeats])

@api.get("/earners/{earner_name}/heartbeats/", response=List[EarnerHeartBeatOutSchema])
def list_heartbeats(request, earner_name: str):
    lastest_heartbeats = EarnerHeartBeat.objects.filter(earner__name=earner_name).values('machine').annotate(
        latest_heartbeat=Max('created_at'))
    return EarnerHeartBeat.objects.filter(created_at__in=[entry['latest_heartbeat'] for entry in lastest_heartbeats])


@api.post("/machines/{machine_name}/{earner_id}/heartbeat/")
def create_heartbeat(request, machine_name: str, earner_id: str, payload: EarnerHeartBeatInSchema):
    machine = Machine.objects.get(pk=machine_name)
    earner = Earner.objects.get_or_create(pk=earner_id)[0]
    EarnerHeartBeat.objects.create(**payload.dict(), machine=machine, earner=earner)
    return {"message": "received"}

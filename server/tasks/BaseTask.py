from sqlmodel import Session, select

from database import engine
from models import Earner


class BaseTask():
    name = "Base Task"
    cron = "0 0 * * *"
    settings = {}
    database = Session()

    def __init__(self):
        # get the eaners settings from the database
        with Session(engine) as session:
            earners = session.exec(select(Earner)).all()
            for earner in earners:
                if earner.id == self.earner_id:
                    self.settings = earner.settings


    def check_requirements(self):
        pass

    def run(self):
        if not self.check_requirements():
            return False
        pass

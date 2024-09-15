from tasks.BaseTask import BaseTask
from tasks.apis.HoneyGainAPI import HoneyGainAPI


class HoneyGainTask(BaseTask):
    name = "HoneyGain Task"
    cron = "0 0 * * *"
    earner_id = "HoneyGain"

    def check_requirements(self):
        if not self.settings.get("email") or not self.settings.get("password"):
            return False
        return True

    def run(self):
        print("Running HoneyGain task")
        honeygain = HoneyGainAPI(self.settings.get("email"), self.settings.get("password"))
        print("login")
        access_token = honeygain.get_access_token()
        print(honeygain.get_honeygain_balance(access_token))
        print(honeygain.claim_pot_reward(access_token))
        return True

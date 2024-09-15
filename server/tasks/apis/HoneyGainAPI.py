import random
import sys
import requests


class HoneyGainAPI:
    email = None
    password = None

    TOKEN = '/users/tokens'
    BALANCE = '/users/balances'
    POT = '/contest_winnings'

    BASE_URL = 'https://dashboard.honeygain.com/api/v1'

    # Random User-Agent generator (simple list of User-Agents for example purposes)
    USER_AGENT = random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
    ])

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_headers(self, access_token):
        return {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'User-Agent': self.USER_AGENT
        }

    def get_access_token(self):
        url = self.BASE_URL + self.TOKEN
        payload = {
            'email': self.email,
            'password': self.password
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Will raise HTTPError for bad responses
            return response.json()['data']['access_token']
        except requests.exceptions.HTTPError as error:
            print('Couldn\'t log into Honeygain 🐝')
            error_msg = str(error)

            if '401' in error_msg:
                print('Email and password is incorrect or not supplied \nCheck credentials and try again')
                sys.exit(1)
            elif '429' in error_msg:
                print('Server is blocking requests due to many attempts \nTry again in a few hours')
                sys.exit(1)
            print(f'Error logging in: {error_msg}')
            raise


    def get_honeygain_balance(self, access_token):
        url = self.BASE_URL + self.BALANCE

        try:
            response = requests.get(url, headers=self.get_headers(access_token))
            response.raise_for_status()
            current_balance = response.json()['data']['payout']['credits']
            print(
                f'Current balance {current_balance}credits 🐝')
            return current_balance
        except requests.exceptions.HTTPError as error:
            print(f'Error fetching balance: {error}')
            raise


    def claim_pot_reward(self, access_token):
        url = self.BASE_URL + self.POT

        try:
            response = requests.post(url, headers=self.get_headers(access_token))
            response.raise_for_status()
            claimed_amount = response.json()['data']['credits']
            print(
                f'Claimed {claimed_amount}credit(s) ✅')
        except requests.exceptions.HTTPError as error:
            error_msg = str(error)
            if '400' in error_msg:
                print(f'Not enough traffic shared to claim reward ❌')
                sys.exit(2)
            elif '403' in error_msg:
                print(f'Already claimed reward pot today ❌')
                return
            print(f'Error claiming pot reward: {error_msg}')
            raise


    def get_winning_credits(self, access_token):
        url = self.BASE_URL + self.POT

        try:
            response = requests.get(url, headers=self.get_headers(access_token))
            response.raise_for_status()
            won_today = response.json()['data'].get('winning_credits', 0)
            print(f'Won today {won_today} credits  🪙')
        except requests.exceptions.HTTPError as error:
            print(f'Error getting winning credits: {error}')
            raise

if __name__ == '__main__':
    honeygain = HoneyGainAPI('email', 'password')
    token = honeygain.get_access_token()
    print(honeygain.get_honeygain_balance(token))
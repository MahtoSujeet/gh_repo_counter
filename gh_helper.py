import requests
import os

class Bot:

    def __init__(self) -> None:
        self.chat_id = os.getenv("chat_id")
        self.bot_token = os.getenv("bot_token")

    def fetch_repos(self, username):
        res = requests.get(f"https://api.github.com/users/{username}/repos")
        print("fetched repos")
        try:
            repos = [ repo["name"] for repo in res.json() ]
            return repos
        except Exception:
            print(res.json())
            self.send_msg("Some Exception happened, there might be new repo created!")

    def send_msg(self, text):
        requests.get(f"https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={text}")
        print("msg sent on telegram")



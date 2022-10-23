from exchange.main import Exchange
from oracle.main import Oracle

class Client:
    def init(self, rpc: str = "https://api.devnet.solana.com", env: str = "devnet", private_key: str = None):
        self.rpc = rpc
        self.env = env

class Zeta:
    def init(self, rpc: str = "https://api.devnet.solana.com", env: str = "devnet", private_key: str = None):
        self.client = Client(rpc, env, private_key)
        self.key = private_key
        self.oracle = Oracle(private_key, self.client)
        self.exchange = Exchange(private_key, self.client)
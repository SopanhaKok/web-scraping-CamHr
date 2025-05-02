from rnet import Impersonate, Client

class Extractor:
    def __init__(self):
        self.session = Client()
        self.session.update(
            Impersonate=Impersonate.Firefox136
        )

    async def fetch_json_async(self,url):
        res = await self.session.get(url)
        return await res.json()
import httpx


class PolymarketClient:
    def __init__(self, http):
        self.http = httpx.AsyncClient()

    async def aclose(self):
        await self.http.aclose()


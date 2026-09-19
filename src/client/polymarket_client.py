import httpx


class PolymarketHttpClient:
    def __init__(self, http):
        self.http = httpx.AsyncClient()

    async def aclose(self):
        await self.http.aclose()


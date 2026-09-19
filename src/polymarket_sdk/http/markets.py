from pydantic import BaseModel, Field, Json

from polymarket_sdk import PolymarketHttpClient

GET_MARKET_BY_ID_URL =  "https://gamma-api.polymarket.com/markets/{id}"


class PolymarketMarket(BaseModel):
    market_id: int = Field(alias="id")
    condition_id: str = Field(alias="conditionId")
    asset_ids: Json[tuple[int, ...]] = Field(alias="clobTokenIds")
    slug: str | None = None
    question: str | None = None
    game_start_time: str | None = Field(default=None, alias="gameStartTime")
    end_date: str | None = Field(default=None, alias="endDate")

async def get_market_by_id(http_client: PolymarketHttpClient, market_id: int):
    r = http_client.http.get(GET_MARKET_BY_ID_URL.format(id = market_id))
    
    if r.status_code != 200:
        raise RuntimeError(
            f"Failed to fetch market {market_id}: HTTP {r.status_code}"
        )
        
    market = PolymarketMarket.model_validate(r.json())
    return market
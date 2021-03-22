from pydantic import BaseModel


class TickerModel(BaseModel):
    id: int
    name: str


class TickerBundleModel(BaseModel):
    tickers: list[TickerModel]

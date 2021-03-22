import json

from .constants import CHAT, DATA, SEARCH, TICKER, NAME, TYPE


def send_search(ws, chat_id, ticker):
    return ws.send(
        json.dumps(
            {
                TYPE: SEARCH,
                DATA: {CHAT: chat_id, TICKER: {NAME: ticker}},
            }
        )
    )

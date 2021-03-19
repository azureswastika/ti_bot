from websocket import WebSocketApp, enableTrace

from core import Mongo

mongo = Mongo()
tickers = mongo.get_collection("tickers")


class Streaming:
    def __init__(self, host="127.0.0.1", port=3000, traceability=False) -> None:
        self.ws = WebSocketApp(
            f"ws://{host}:{port}",
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        if traceability:
            enableTrace(True)

    def run(self):
        """Run websocket"""
        self.ws.run_forever()

    def on_open(self, ws: WebSocketApp):
        """On websocket open"""

    def on_message(self, ws: WebSocketApp, message: str):
        """On websocket message"""

    def on_error(self, ws: WebSocketApp, error: str):
        """On websocket error"""
        print(error)

    def on_close(self, ws: WebSocketApp):
        """On websocket close"""


if __name__ == "__main__":
    main = Streaming()
    main.run()

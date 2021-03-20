from threading import Thread

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater
from websocket import WebSocketApp, enableTrace


class Listener:
    def __init__(self, host="127.0.0.1", port=3000, traceability=False) -> None:
        from os import environ

        self.ws = WebSocketApp(
            f"ws://{host}:{port}",
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        if traceability:
            enableTrace(True)

        self.updater = Updater(environ.get("TG_TOKEN"))
        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("ticker", self.ticker))

    def run(self):
        """Run websocket"""
        Thread(target=self.ws.run_forever).start()
        Thread(target=self.updater.start_polling).start()
        self.updater.idle()

    def start(self, update: Update, _: CallbackContext):
        update.message.reply_text(
            "Use /subscribe <ticker> to subscribe on the ticker changes"
        )

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
    main = Listener()
    main.run()

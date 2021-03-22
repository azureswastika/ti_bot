import json
from threading import Thread

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater
from websocket import WebSocketApp, enableTrace

from core import TickerModel, tickers
from core.funtions import send_search


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
        self.dispatcher.add_handler(CommandHandler("subscribe", self.subscribe))
        self.dispatcher.add_handler(CommandHandler("unsubscribe", self.unsubscribe))

    def run(self):
        """Run websocket"""
        Thread(target=self.ws.run_forever).start()
        Thread(target=self.updater.start_polling).start()
        self.updater.idle()

    def start(self, update: Update, _: CallbackContext):
        update.message.reply_text(
            (
                "Use /subscribe <ticker> to subscribe on the ticker changes\n"
                "Use /unsubscribe <ticker> to unsubscribe on the ticker changes"
            )
        )

    def subscribe(self, update: Update, _: CallbackContext):
        chat_id = update.message.chat_id
        ticker = update.message.text.split()[1].upper()
        if ticker.isalpha():
            if ticker_obj := tickers.get({"name": ticker}):
                return update.message.reply_text(
                    "You have subscribed to {}".format(ticker_obj["name"])
                )
            return send_search(self.ws, chat_id, ticker)
        return update.message.reply_text("Incorrect ticker format")

    def unsubscribe(self, update: Update, _: CallbackContext):
        pass

    def on_open(self, ws: WebSocketApp):
        """On websocket open"""

    def on_message(self, ws: WebSocketApp, message: str):
        """On websocket message"""
        message = json.loads(message)
        if message["type"] == "search":
            ticker = TickerModel(**message["data"]["ticker"]).dict()
            tickers.create(ticker)

    def on_error(self, ws: WebSocketApp, error: str):
        """On websocket error"""
        print(error)

    def on_close(self, ws: WebSocketApp):
        """On websocket close"""


if __name__ == "__main__":
    main = Listener()
    main.run()

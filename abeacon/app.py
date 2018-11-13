# Author: JC
# Date: 2018/11/12 18:54
# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, BeaconEvent
)

app = Flask(__name__)

line_bot_api = LineBotApi('{Channel access token (long-lived}')
handler = WebhookHandler('{Channel Secret}')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text  # message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))  # reply the same message from user


@handler.add(BeaconEvent)
def handle_beacon_event(event):
    if event.beacon.hwid == "{your HWId}":
        msg = '{your message 1}'
    else:
        msg = '{your message 2}'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg)

    if __name__ == "__main__":
        app.run()

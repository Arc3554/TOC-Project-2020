import os
import sys

from flask import Flask, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message
from utils import send_img_url

load_dotenv()


machine = TocMachine(
    states=["user", "state1", "state2","state3","state4","state5","state6","state7","state8","state9"],
    transitions=[
        {"trigger": "advance","source": "user","dest": "state1","conditions": "is_going_to_state1"},
        {"trigger": "advance","source": "user","dest": "state2","conditions": "is_going_to_state2"},
        {"trigger": "advance", "source":"user", "dest": "state3","conditions":"is_going_to_state3"},
        {"trigger": "advance", "source":"user", "dest": "state4","conditions":"is_going_to_state4"},
        {"trigger": "advance", "source":"user", "dest": "state5","conditions":"is_going_to_state5"},
        {"trigger": "advance", "source":"user", "dest": "state6","conditions":"is_going_to_state6"},
        {"trigger": "advance", "source":"user", "dest": "state7","conditions":"is_going_to_state7"},
        {"trigger": "advance", "source":"user", "dest": "state8","conditions":"is_going_to_state8"},
        {"trigger": "advance", "source":"user", "dest": "state9","conditions":"is_going_to_state9"},        
        {"trigger": "go_back", "source": ["state1","state2","state3","state4","state5","state6","state7","state8","state9"], "dest": "user"},

    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )
    return "OK"

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        response = machine.advance(event)       
        if event.message.text == "show-fsm": 
            send_img_url(event.reply_token,'https://imgur.com/w3LXqx4.jpg')
            response = True

        if response == False:
            send_text_message(event.reply_token, "請先輸入有興趣的類型\n('日常','戰鬥','劇情','戀愛',\n'穿越','科幻','音樂','熱血')\n\n之後輸入'預覽'即可獲得預覽圖片")
    return "OK"

@app.route("/show-fsm", methods=["GET"])
def show_fsm():   
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
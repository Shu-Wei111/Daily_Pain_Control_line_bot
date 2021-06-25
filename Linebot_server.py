# -*- coding: utf-8 -*-
import configparser
import json

import linebot
from flask import Flask, request, abort
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import main
import Template

app = Flask(__name__)  # 建立 Flask 物件

config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel-access-token'))
handler = WebhookHandler(config.get('line-bot', 'channel-secret'))


@app.route("/callback", methods=['POST'])  # 路由
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text

    if text.find('查看課程') == 0:
        try:
            line_bot_api.push_message(event.source.user_id, Template.page_1)
        except linebot.exceptions.LineBotApiError as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error.message)
            print(e.error.details)
    elif text.find('進入課程') == 0:
        course_template(event.source.user_id,text)
    elif text.find('疼痛測驗') == 0:
        response = 'hi'
    elif text.find('疼痛改善') == 0:
        try:
            response = line_bot_api.push_message(event.source.user_id, Template.symptom_evaluation)
        except linebot.exceptions.LineBotApiError as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error.message)
            print(e.error.details)
    elif text.find('心得回饋') == 0:
        response = '請幫我用以下格式回傳心得\n' \
                   '我的心得:填入您的心得'
    elif text.find('我的心得') == 0:
        response = main.Experience(event.source.user_id, text)
    elif text.find('聯絡老師') == 0:
        response = main.Contact_Teacher()
    elif text.find('註冊') == 0:
        response = '請幫我用以下格式回傳資料\n' \
                   '姓名:填入姓名/學號:填入學號'
    elif text.find('姓名:') == 0 and text.find('') < text.find('/學號:'):
        response = main.Register(event.source.user_id, text)

    else:
        response = '鑷子不懂您在說什麼\n_(:3 」∠ )_'

    # 回覆文字訊息
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=response))


def course_template(user_id, text):
    text = text.split('進入課程')
    page = text[1]
    if page == '2_1':
        try:
            print(page)
            line_bot_api.push_message(user_id, Template.page_2_1)
        except linebot.exceptions.LineBotApiError as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error.message)
            print(e.error.details)


if __name__ == "__main__":
    app.run(debug=True)


# coding: utf-8

# In[ ]:


import requests
import re
import random
import configparser
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('')
handler = WebhookHandler('')


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
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    if event.message.text == "信用卡":
        buttons_template = TemplateSendMessage(
            alt_text='信用卡 template',
            template=ButtonsTemplate(
                title='請選擇您需要的資訊',
                text='點擊選擇',
                thumbnail_image_url='https://i.imgur.com/6Lv0q4f.png',
                actions=[
                    URITemplateAction(
                        label='信用卡介紹',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010101/TS0201010101/index.htm'
                    ),
                    URITemplateAction(
                        label='信用卡權益',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010102/index.htm'
                    ),
                    URITemplateAction(
                        label='VISA金融卡',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010103/index.htm'
                    ),
                    URITemplateAction(
                        label='商戶收單服務',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0201/TS020101/TS02010104/index.htm'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

    if event.message.text == "存款":
        buttons_template = TemplateSendMessage(
            alt_text='存款 template',
            template=ButtonsTemplate(
                title='請選擇您需要的資訊',
                text='點擊選擇',
                thumbnail_image_url='https://i.imgur.com/JdcSRkV.png',
                actions=[
                    URITemplateAction(
                        label='產品介紹',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0202/TS020201/TS02020101/index.htm'
                    ),
                    URITemplateAction(
                        label='理財試算',
                        uri='https://www.taishinbank.com.tw/TS/TS06/TS0604/TS060401/TS06040101/index.htm?optionValue=01&optionValue2=01&urlPath1=TS02&urlPath2=TS0202'
                    ),
                    URITemplateAction(
                        label='存款牌告利率',
                        uri='https://www.taishinbank.com.tw/TS/TS06/TS0605/TS060501/index.htm?urlPath1=TS02&urlPath2=TS0202&optionValue=02'
                    ),
                    URITemplateAction(
                        label='優惠活動',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0295/TS029504/TS02950401/index.htm?input-value1=613158822453020080&input-value2=613158822453020082'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

    if event.message.text == "貸款":
        buttons_template = TemplateSendMessage(
            alt_text='貸款 template',
            template=ButtonsTemplate(
                title='請選擇您需要的資訊',
                text='點擊選擇',
                thumbnail_image_url='https://i.imgur.com/pe1y61i.png',
                actions=[
                    URITemplateAction(
                        label='房貸試算',
                        uri='https://www.taishinbank.com.tw/TS/TS06/TS0604/TS060405/TS06040501/index.htm?optionValue=05&optionValue2=01&urlPath1=TS02&urlPath2=TS0203'
                    ),
                    URITemplateAction(
                        label='信貸產品介紹',
                        uri='https://www.taishinbank.com.tw/TS/TS06/TS0604/TS060404/TS06040401/index.htm?optionValue=04&optionValue2=01&urlPath1=TS02&urlPath2=TS0203'
                    ),
                    URITemplateAction(
                        label='購車貸款',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0203/TS020303/TS02030301/index.htm'
                    ),
                    URITemplateAction(
                        label='股票質押貸款',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0203/TS020304/TS02030404/index.htm'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

    if event.message.text == "投資":
        buttons_template = TemplateSendMessage(
            alt_text='投資 template',
            template=ButtonsTemplate(
                title='請選擇您需要的資訊',
                text='點擊選擇',
                thumbnail_image_url='https://i.imgur.com/dlskzYZ.png',
                actions=[
                    URITemplateAction(
                        label='台新i理財首頁',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0204/iFundNew/FN01/index.htm'
                    ),
                    URITemplateAction(
                        label='產品總覽/淨值查詢',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0204/iFundNew/FN03/index.htm'
                    ),
                    URITemplateAction(
                        label='專家觀點',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0204/iFundNew/FN04/index.htm'
                    ),
                    URITemplateAction(
                        label='投資報告',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0204/iFundNew/FN05/FN0501/index.htm'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

    if event.message.text == "保險":
        buttons_template = TemplateSendMessage(
            alt_text='保險 template',
            template=ButtonsTemplate(
                title='請選擇您需要的資訊',
                text='點擊選擇',
                thumbnail_image_url='https://i.imgur.com/EUya4oo.png',
                actions=[
                    URITemplateAction(
                        label='人壽/年金保險',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0205/TS020506/TS020501/TS02050101_DIS/index.htm'
                    ),
                    URITemplateAction(
                        label='健康保險',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0205/TS020506/TS020502/TS02050201_DIS/index.htm'
                    ),
                    URITemplateAction(
                        label='意外險/產險',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0205/TS020506/TS020503/TS02050301_DIS/index.htm'
                    ),
                    URITemplateAction(
                        label='投資險',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0205/TS020506/TS020504/TS02050401_DIS/index.htm'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)

    if event.message.text == "財富管理":
        buttons_template = TemplateSendMessage(
            alt_text='財富管理 template',
            template=ButtonsTemplate(
                title='請選擇您需要的資訊',
                text='點擊選擇',
                thumbnail_image_url='https://i.imgur.com/PWM8Z8a.png',
                actions=[
                    URITemplateAction(
                        label='最新消息',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0299/TS029901/TS02990102/index.htm?input-value1=613158822453005203'
                    ),
                    URITemplateAction(
                        label='全方位服務禮遇',
                        uri='https://www.taishinbank.com.tw/TS/TS02/TS0206/TS020606/index.htm'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)


if __name__ == "__main__":
    app.run()

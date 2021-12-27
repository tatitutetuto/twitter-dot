from linebot import LineBotApi
from linebot.models import TextMessage
import os
from dotenv import load_dotenv
load_dotenv()

class Line:
    def send_message(self, e):
        # LINEに必要なアクセストークンと、ユーザID取得
        CHANNEL_ACCESEE__TOKEN = os.environ['CHANNEL_ACCESEE__TOKEN']
        USER_ID = os.environ['USER_ID']
        line_bot_api = LineBotApi(CHANNEL_ACCESEE__TOKEN)

        # メッセージ
        messages = TextMessage(
            text = '【TWITTER_DOTにてエラー】\n下記内容を確認してください\n\n{}'.format(e)
        )

        # 送信
        line_bot_api.push_message(USER_ID, messages=messages)


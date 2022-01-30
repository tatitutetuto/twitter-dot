from bs4 import BeautifulSoup
import requests
import config
import datetime

from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import json
import os
from dotenv import load_dotenv
load_dotenv()

class Scraping:

    ##
    ## CoinMarketCapよりスクレイピングして情報取得
    ##
    def get_dot_info(self):
        # APIでDOTの情報取得
        cmc = CoinMarketCapAPI(os.environ.get('COIN_MARKET_CAP_API_KEY'))
        print("cmc:" + str(cmc))
        res = cmc.cryptocurrency_quotes_latest(id=6636, convert='JPY')
        # print(res)

        # json形式に変更
        res = str(res.data).replace("'", '"') .replace('None', '"None"')
        data = json.loads(res)
        # print(data)

        # 価格取得、小数点第3位を四捨五入
        correct_price = float(data["6636"]["quote"]["JPY"]["price"])
        price = round(correct_price, 2)
        print(f'ポルカドットの価格は現在{price}円です')

        # コインマーケットキャップ内の時価総額取得
        cmc_rank = data["6636"]["cmc_rank"]   
        print(f'ポルカドットの時価総額ランキングは現在{cmc_rank}位です')

        # 24時間前との値段比較、小数点第3位を四捨五入
        correct_percent_change_24h = float(data["6636"]["quote"]["JPY"]["percent_change_24h"])
        percent_change_24h = round(correct_percent_change_24h, 2)
        if percent_change_24h > 0:
            print(f'ポルカドットの値段は24時間前に比べて{percent_change_24h}%上がっています')

        else:
            print(f'ポルカドットの値段は24時間前に比べて{percent_change_24h}%下がっています')

        return price, cmc_rank, percent_change_24h


    ##
    ## ポルカドットの関連ニュースを取得する
    ##
    def get_news_url(self):
        # 変数初期化
        update_flg = False
        article_title = ''
        news_url = ''

        #　スクレイピング準備
        res = requests.get(config.BITTIMES_URL)
        soup = BeautifulSoup(res.text, 'html.parser')

        # 表示される記事数を取得
        article_items = soup.find_all('div', class_='post-list')
        index = len(soup.find_all('div', class_='post-list'))

        # 現在時刻から-3時間までの時刻を取得
        date_time = datetime.datetime.now()
        date_time_m1 = date_time + datetime.timedelta(hours=-1)
        date_time_m1 = date_time_m1.strftime("%Y/%m/%d %H")

        date_time_m2 = date_time + datetime.timedelta(hours=-2)
        date_time_m2 = date_time_m2.strftime("%Y/%m/%d %H")
        
        date_time_m3 = date_time + datetime.timedelta(hours=-3)
        date_time_m3 = date_time_m3.strftime("%Y/%m/%d %H")

        # date_time = '2021/12/20 18'

        # 取得記事のループ
        for i in range(index):
            # 記事の更新時刻を加工
            article_date = soup.find_all('time')[i].text
            idx = article_date.find(':')
            article_date = article_date[:idx] 

            # 存在する場合
            if article_date == date_time or article_date == date_time_m1 or article_date == date_time_m2 or article_date == date_time_m3:
                
                # タイトル、URLを取得
                news_url = article_items[i].a.get("href")
                article_title = article_items[i].img.get('alt')
                update_flg = True


        print(update_flg)
        print(article_title)
        print(news_url)

        return update_flg, article_title, news_url
    

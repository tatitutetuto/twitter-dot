from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
import json
import os
from dotenv import load_dotenv
load_dotenv()

class Scraping:
    def get_dot_info(self):
        # APIでDOTの情報取得
        cmc = CoinMarketCapAPI(os.environ['COIN_MARKET_CAP_API_KEY'])
        # AK = os.environ['COIN_MARKET_CAP_API_KEY']
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
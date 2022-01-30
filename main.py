import scraping as sp
import twitter as tw
import line as ln

def main():
    try:
        # 値段、時価総額ランクを取得
        scraping = sp.Scraping()
        price, cmc_rank, percent_change_24h = scraping.get_dot_info()

        # bittimesニュースを取得
        bittimes_update_flg, bittimes_news_title, bittimes_news_url = scraping.get_bittimes_news()
        
        # Yahooニュースを取得
        yahoo_update_flg, yahoo_news_title, yahoo_news_url = scraping.get_yahoo_news()
        
        # BITTIMESの記事をツイートする
        twitter = tw.Twitter(price, cmc_rank, percent_change_24h, bittimes_news_title, bittimes_news_url, yahoo_news_title, yahoo_news_url)
        if bittimes_update_flg == True:
            twitter.tweet_dot_news()
            
        # Yahoo記事をツイートする
        if yahoo_update_flg == True:
            twitter.tweet_dot_news()

        # ポルカドットの情報をツイートする
        twitter.tweet_dot_info()

        # リツイートする
        # twitter.retweet()

        # DMをLINEで通知する
        # twitter.info_direct_message()
        

    except Exception as e:
        print(e)
        
        # エラー内容LINE通知
        line = ln.Line()
        line.send_message(e)

if __name__ == '__main__':
    main()

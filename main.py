import scraping as sp
import twitter as tw
import line as ln

def main():
    try:
        # 値段、時価総額ランクを取得
        scraping = sp.Scraping()
        price, cmc_rank, percent_change_24h = scraping.get_dot_info()

        # ニュース情報を取得
        update_flg, news_title, news_url = scraping.get_news_url()
        scraping.get_news_url()

        # ポルカドットの情報をツイートする
        twitter = tw.Twitter(price, cmc_rank, percent_change_24h, news_title, news_url)
        twitter.tweet_dot_info()

        # ポルカドットの記事をツイートする
        if update_flg == True:
            twitter.tweet_dot_news()

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

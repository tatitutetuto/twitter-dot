import scraping as sp
import twitter as tw
import line as ln

def main():
    try:
        # 値段、時価総額ランクを取得
        scraping = sp.Scraping()
        price, cmc_rank, percent_change_24h = scraping.get_dot_info()

        # ツイートする
        twitter = tw.Twitter(price, cmc_rank, percent_change_24h)
        twitter.tweet_dot_info()

        # リツイートする
        twitter.retweet()

        # DMをLINEで通知する
        # twitter.info_direct_message()


    except Exception as e:
        print(e)
        
        # エラー内容LINE通知
        line = ln.Line()
        line.send_message(e)

if __name__ == '__main__':
    main()
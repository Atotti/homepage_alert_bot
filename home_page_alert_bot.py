from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time
import datetime
import csv
import pprint


while (True):
    try:
        # ブラウザーを起動
        options = Options()
        options.binary_location = r'chromeのパス'
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        driver.get('http://www.toyotama-h.metro.tokyo.jp/site/zen/')

        

        time.sleep(5)

        # htmlを取得
        html = driver.page_source

        #print("============================================================================================================")
        #print(html)

        #print("====================================================================================")

        time.sleep(5)

        news = driver.find_element_by_class_name("m-list_news").text

        #print(news)

        news_url = driver.find_element_by_xpath('//*[@id="l-main"]/div[1]/dl/dd[1]/a').get_attribute("href")

        #print(news)

        

        newss = news.split(',')
        with open('new_HP_news.csv', 'w') as f: 
            writer = csv.writer(f)
            writer.writerow(newss)

        #old_HP_news = news

        #old_HP_news = old_HP_news.split(',')
        #with open('old_HP_News.csv','w') as f:
        #    witer = csv.writer(f)
        #    witer.writerow(old_HP_news)



        with open('old_HP_News.csv', mode="r") as f:
            reader = csv.reader(f)
            old_HP_News = '' 
            for r in reader:
                tex = ''.join(r)
                old_HP_News += tex

        with open('new_HP_News.csv', mode="r") as f:
            reader = csv.reader(f)
            new_HP_News = '' # ←ここで変数を宣言し初期化する
            for r in reader:
                tex = ''.join(r)
                new_HP_News += tex

        #print(old_HP_News)
        #print(new_HP_News)

        driver.quit()

        #ツイートを生成

        #print("=======--")
        
        tweet1 = new_HP_News.split()

        tweet = tweet1[:2]
        #print(tweet)

        tweet = str(tweet) + news_url

        print(tweet)
        

        if not (old_HP_News == new_HP_News):
            options = Options()
            options.binary_location = r'クロームのパス'
            options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)

            driver.get('https://twitter.com/login')

            driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys("TwitterのID")

            driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys("TwitterのPASS")

            driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()

            driver.implicitly_wait(10)

            driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').send_keys(tweet)

            driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]').click()

            html = driver.page_source

            old_HP_news = new_HP_News

            old_HP_news = old_HP_news.split(',')
            with open('old_HP_News.csv','w') as f:
                witer = csv.writer(f)
                witer.writerow(old_HP_news)


            driver.quit()
            print("アラートを出す")
            print("オールドを更新する")
        else:
            print("なにもしない")
        

    except:
        print("やり直す")
        continue
        
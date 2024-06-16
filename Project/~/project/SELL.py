from bs4 import BeautifulSoup
import time
from playsound import playsound
from selenium import webdriver

driver = webdriver.Chrome()
list = []
dict={}
for i in range(45):
    time.sleep(120)
    for baz in list:
        time.sleep(1)
        wer = baz + '/'
        ans = 'https://finance.yahoo.com/quote/' + wer

        driver.get(ans)

        html_text = driver.page_source
        soup = BeautifulSoup(html_text, 'lxml')
        current = soup.find('fin-streamer', class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").text
        current = current.replace(",", "")
        izInt = True
        try:
            float(current)
        except ValueError:
            izInt = False
        if izInt:
            if baz in dict:
                if dict[baz] <= current:
                    dict[baz] = current
                else:

                    playsound(r'C:\Users\arcan\Downloads\gg.mp3')
                    print(baz)
                    list.remove(baz)
            else:
                dict[baz]=current
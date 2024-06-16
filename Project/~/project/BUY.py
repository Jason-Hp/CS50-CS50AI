from bs4 import BeautifulSoup
import time
from playsound import playsound
from selenium import webdriver
def main():


    # TODO: Read database file into a variable

    driver = webdriver.Chrome()

    list = ['SPIR','MAPS','HCTI','VGFC','SYTA','NAOV','MOBQ','APGN']
    dict = {}
    ulist = []
    flist = []
    for ind in list:
        time.sleep(3)
        wer = ind + '/'
        ans = 'https://finance.yahoo.com/quote/' + wer


        driver.get(ans)

        html_text = driver.page_source
        soup = BeautifulSoup(html_text, 'lxml')
        TEST = soup.find('td', class_="Ta(end) Fw(600) Lh(14px)")

        if TEST != None:
            sot = soup.findAll('td', class_="Ta(end) Fw(600) Lh(14px)")
            close = sot[0].text
            open = sot[1].text

            close = close.replace(",", "")
            open = open.replace(",", "")

            isInt = True
            try:
                float(close)
            except ValueError:
                isInt = False
            if isInt:



                close = float(close)
                open = float(open)

                if open>close :
                    ulist.append(ind)
                    dict[ind] = open

    time.sleep(240)
    for gee in ulist:
        time.sleep(1)
        wer = gee + '/'
        ans = 'https://finance.yahoo.com/quote/' + wer


        driver.get(ans)

        html_text = driver.page_source
        soup = BeautifulSoup(html_text, 'lxml')

        current = soup.find('fin-streamer', class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").text
        current = current.replace(",", "")
        isInt = True
        try:
            float(current)
        except ValueError:
            isInt = False
        if isInt:
            current = float(current)
            if dict[gee]>=current:
                flist.append(gee)
                dict[gee] = current


    for i in range(45):
        time.sleep(120)
        for baz in flist:
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
                if dict[baz]>=current:
                    dict[baz]=current
                else:

                    playsound(r'C:\Users\arcan\Downloads\gg.mp3')
                    print(baz)
                    flist.remove(baz)



main()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import random
import schedule
from time import sleep
a = str(input("e-mailアドレスを入力してください:"))
b = str(input("パスワードを入力してください:")) 
c = str(input("クラスを入力してください(全角で～組(例：３組)):")) #
d = str(input("番号を入力してください(半角で数字だけ入力し、一桁の場合は07のように十のくらいに0を付けてください。):")) #
e = str(input("名前を入力してください:")) #
print("36.a~36.bまでのランダムな体温を送ります。") #
f = float(input("a:")) #
g = float(input("b:")) #
h = str(input("毎日何時に送信しますか？（半角で06:18のように入力してください）:")) #
print("初期設定完了!")
time.sleep(1)
print("このプログラムを走らせ続けている限りいま入力した設定は変わりません。")
time.sleep(1)
print("もしも変更したい場合はプログラムを終了し、もう一度走らせてください。")
time.sleep(1)
print("それでは、体温自動入力機能を起動します。")
def nyuuryoku():
    # website   = 'https://accounts.google.com/v3/signin/identifier?dsh=S-1374848447%3A1676210900940333&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSdC01s_lWvkUbDZV1ADZDJc8EBHxEezTZ_hy2RoXRSWFomFGQ%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSdC01s_lWvkUbDZV1ADZDJc8EBHxEezTZ_hy2RoXRSWFomFGQ%2Fviewform&ltmpl=forms&osid=1&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHcTDs6PP8qpx67kTMN-IPeRpsGO7S3mOQpvIYKl3t9m5DlGO0DTsEp1IW-CJJSie08ht_c7sw'
    #=================================================
    website = 'https://accounts.google.com/v3/signin/identifier?dsh=S923230193%3A1676901443827549&continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSdC01s_lWvkUbDZV1ADZDJc8EBHxEezTZ_hy2RoXRSWFomFGQ%2FformResponse%3F%26entry.1882723041%3D' + d + '&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSdC01s_lWvkUbDZV1ADZDJc8EBHxEezTZ_hy2RoXRSWFomFGQ%2FformResponse%3F%26entry.1882723041%3D22&ltmpl=forms&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHcgi-UzAKKEk4xZFf-SFSUErIORZGBe6b8xN1TqfSS1MDYqoXZlKJyD7hcfYVkiZckkM_XwqQ' + d
    #chromeを開く
    # &entry.1882723041=22
    chro = webdriver.Chrome()
    chro.get(website)
    
    if(chro.current_url==website):
        time.sleep(3)
        #テキスト入力
        input = chro.find_element(By.ID,'identifierId')
        input.send_keys(a)
        print("e-mail入力完了 ・・")

        time.sleep(1)

        inpu = chro.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button')
        inpu.click()
        print("次へ・・")
        
        time.sleep(3)

        input1 = chro.find_element(By.NAME,'Passwd')
        input1.send_keys(b)
        print("パスワード入力完了・・")

        time.sleep(1)

        inpu1 = chro.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button')
        inpu1.click()
        print("フォームへ移動・・")

        time.sleep(10)

        # inp = chro.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[2]/div')
        # inp.click()
        # print("フォームをクリア・・")

        # time.sleep(3)

        # inp1 = chro.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span')
        # inp1.click()
        # print("フォームのクリアを許可・・")

        # time.sleep(3)
        
        date = datetime.datetime.now()
        hi = date.day
        if hi < 10:
            hi =  0 + hi
        else:
            hi = hi
        tuki = date.month
        if tuki < 10:
            tuki = 0 + tuki
        else:
            tuki = tuki
        date = str(date.year) + str(tuki) + str(hi) 
        input2 = chro.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        input2.send_keys(date)
        print("年月日を入力・・")
        
        time.sleep(3)

        input3 = chro.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]')
        input3.send_keys(c)
        print("クラスを入力・・")

        time.sleep(1)

        
        # input4 = chro.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
        # input4 = chro.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]')
        # input4.send_keys(d)
        # p = str(d+2)
        # number = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[' + p +']'
        # print(number)
        # inputl = chro.find_element(By.XPATH,number)
        # print(number)
        # time.sleep(3)
        # inputl.send_keys(2)
        # inputl.send_keys(2)
        # inputl.submit()
        # print("番号を入力 ・・")

        time.sleep(1)

        input5 = chro.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        input5.send_keys(e)
        print("名前を入力・・")

        time.sleep(1)

        randamu = int(random.uniform(f,g))
        taionn = "36." + str(randamu)
        input6 = chro.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]')
        input6.send_keys(taionn)
        print("ランダムな体温を入力・・")

        time.sleep(1)

        input7 = chro.find_element(By.XPATH,'//*[@id="i26"]')
        input7.click()
        print('体調の不良・良好を選択・・')
        
        input8 = chro.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        input8.click()
        print('送信画面へ移動・・')

        time.sleep(3)
        input9 = chro.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
        input9.click()
        print('送信成功!')

        time.sleep(3)
        chro.quit()

        print('また明日!')

schedule.every().days.at(h).do(nyuuryoku)

while True:
    schedule.run_pending()
    sleep(1)

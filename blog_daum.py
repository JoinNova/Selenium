from time import sleep
from selenium import webdriver
from random import *
while 1:
    browser = webdriver.Chrome(executable_path=r"/Users/nova/git/chromedriver")
    browser.set_window_size(960, 200)
    i=0
    while 1:
        i+=1
        browser.get('https://www.daum.net/')
        sleep(uniform(1.0, 2.5))
        k=randint(0,11)
        sr = "백준알고리즘 "+['boj10943','난제','신용카드','문자열폭발','팰린드롬 boj10235','대소문자',
                        '카이사르5598','골드바흐의 추측 boj 9020','감소하는수','랜덤','10993','일반화학실험'][k]
        #PW = "사용자비밀번호"
        elem_search = browser.find_element_by_name("q")
        elem_search.send_keys(sr)

        #elem_login = browser.find_element_by_name("login_password")
        #elem_login.send_keys(PW)
        sleep(uniform(1.0, 3.5))
        browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]').click()
        path=['//*[@id="blogColl"]/div[2]/ul/li[2]/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[1]/div[1]/div/a',
              '//*[@id="blogColl"]/div[2]/ul/li[1]/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[2]/div[1]/div/a',
              '//*[@id="blogColl"]/div[2]/ul/li[2]/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[1]/div[1]/div/a',
              '//*[@id="blogColl"]/div[2]/ul/li[2]/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[3]/div[1]/div/a',
              '//*[@id="blogColl"]/div[2]/ul/li[2]/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[1]/div[1]/div/a'
              '//*[@id="blogColl"]/div[2]/ul/li/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[1]/div[1]/div/a'][k]
        sleep(uniform(0.5, 3.5))
        browser.find_element_by_xpath(path).click()
        sleep(uniform(1.0, 3.5))
        
        top=500;bottom=randint(100,1000)
        browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
        sleep(uniform(1.0, 1.5))
        if i==10:break

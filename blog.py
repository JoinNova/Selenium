from time import sleep
from selenium import webdriver
from random import *
while 1:
    browser = webdriver.Chrome(executable_path=r"/home/nova/git/chromedriver")
    browser.set_window_size(960, 200)
    i=0
    while 1:
        i+=1
        browser.get('https://www.naver.com/')
        sleep(uniform(1.0, 2.5))
        k=randint(0,4)
        sr = "백준알고리즘 "+['소수','피보나치','난제','스타트링크','별 찍기'][k]
        #PW = "사용자비밀번호"
        elem_search = browser.find_element_by_name("query")
        elem_search.send_keys(sr)

        #elem_login = browser.find_element_by_name("login_password")
        #elem_login.send_keys(PW)
        sleep(uniform(1.0, 3.5))
        browser.find_element_by_xpath('//*[@id="search_btn"]').click()
        path=['//*[@id="sp_blog_4"]/dl/dt/a','//*[@id="sp_blog_3"]/dl/dt/a','//*[@id="web_layer_2"]/dl/dt/a',
              '//*[@id="sp_blog_1"]/dl/dt/a','//*[@id="sp_blog_4"]/dl/dt/a'][k]
        sleep(uniform(0.5, 3.5))
        browser.find_element_by_xpath(path).click()
        sleep(uniform(1.0, 3.5))
        
        top=500;bottom=randint(100,1000)
        browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
        sleep(uniform(1.0, 1.5))
        if i==10:break


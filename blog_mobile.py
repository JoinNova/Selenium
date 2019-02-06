from time import sleep
from selenium import webdriver
from random import *
from selenium import webdriver


while 1:
    
    browser = webdriver.Chrome(executable_path=r"/Users/nova/git/chromedriver")
    browser.set_window_size(375, 812)
    i=0
    while 1:
        i+=1
        browser.get('https://m.naver.com/')
        sleep(uniform(1.0, 2.5))
        k=randint(0,26)
        sr = "백준알고리즘 "+['boj10943','난제','신용카드','문자열폭발','팰린드롬','대소문자',
                        '카이사르','골드바흐','감소하는수','랜덤','10993','일반화학실험','크로스워드','8진수',
                        '명령프롬프트','보물','다이나믹','파일완전삭제','좋아해','누울','fro','2의제곱','저작권',
                        '소수찾기','rot','아','별 찍기'][k]
        #PW = "사용자비밀번호"
        elem_search = browser.find_element_by_name("query")
        elem_search.send_keys(sr)
        browser.find_element_by_xpath('//*[@id="search"]/button/span').click()
        #elem_login = browser.find_element_by_name("login_password")
        #elem_login.send_keys(PW)
        sleep(uniform(0.5, 2.5))
        path=['//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div[1]/a',
              '//*[@id="web_3"]/div/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',
              '//*[@id="web_1"]/div/a','//*[@id="web_1"]/div/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div[1]/a',
              '//*[@id="web_2"]/div/a','//*[@id="web_1"]/div/a','//*[@id="web_1"]/div/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',
              '//*[@id="web_1"]/div/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div[1]/a',
              '//*[@id="web_1"]/div/a','//*[@id="web_4"]/div/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',
              '//*[@id="web_2"]/div/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[4]/div[1]/a',
              '//*[@id="web_1"]/div/a','//*[@id="web_1"]/div/a',
              '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[4]/div[1]/a'][k]
        sleep(uniform(0.5, 2.5))
        browser.find_element_by_xpath(path).click()
        sleep(uniform(0.5, 2.5))
        
        #top=500;bottom=randint(100,1000)
        #browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
        sleep(uniform(0.5, 1.5))
        if i==3:break

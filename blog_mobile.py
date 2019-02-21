from time import sleep
from selenium import webdriver
from random import *
from selenium import webdriver


while 1:
    try:
        browser = webdriver.Chrome(executable_path=r"/Users/nova/git/chromedriver")
        browser.set_window_size(375, 812)
        i=0
        while 1:
            i+=1
            browser.get('https://m.naver.com/')
            sleep(uniform(1.0, 1.5))
            k=randint(0,64)
            sr = "백준 알고리즘 "+['난제','행운의편지','if','비슷한단어','super','strange','quarters','지각','N과M','골드바흐',
                             '타일링','피터팬','Z','청기','만취한','gcd','탈출','역배치','스테판','한조',
                             'key','부분합','숨바꼭질','dslr','팰린드롬','수묶기','회의실배정','부분문자열','contest','시간초과',
                             '탑','쇠막대기','엄청난','정렬','중복','좌표','수정렬','주사위 세개','개수세기','스타트링크',
                             '줄세우기','문자열폭발','군계일학','소수구하기','이상한기호','casio','babba','01','돌게임6','랜덤',
                             '삼각형','카카오','상금','sort','밑줄','부분수열','부분집합','시험감독','2차원','보물',
                             '암호','이상한','연세대학교','신용카드','입실'][k]
            #PW = "사용자비밀번호"
            elem_search = browser.find_element_by_name("query")
            elem_search.send_keys(sr)
            browser.find_element_by_xpath('//*[@id="search"]/button/span').click()
            #elem_login = browser.find_element_by_name("login_password")
            #elem_login.send_keys(PW)
            sleep(uniform(0.5, 1.5))
            path=['//*[@id="web_3"]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div[1]/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#05
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',
                  '//*[@id="web_1"]/div/a',
                  '//*[@id="web_2"]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',#10
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',#'타일링','피터팬','Z','청기','만취한','gcd','탈출','역배치','스테판','한조'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',
                  '//*[@id="web_2"]/div/a',#15
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',
                  '//*[@id="web_3"]/div/a',
                  '//*[@id="web_1"]/div/a',#18
                  '//*[@id="web_1"]/div/a',
                  '//*[@id="web_1"]/div/a',#20
                  '//*[@id="web_1"]/div/a',
                  '//*[@id="web_1"]/div/a',#22'숨바꼭질','dslr',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div/a',
                  '//*[@id="web_2"]/div/a',#24'팰린드롬','수묶기','회의실배정','부분문자열','contest','시간초과'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',
                  '//*[@id="web_1"]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',
                  '//*[@id="web_1"]/div/a',#28
                  '//*[@id="web_1"]/div/a',#29
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',
                  '//*[@id="web_2"]/div/a',#31'탑','쇠막대기','엄청난','정렬','중복','좌표','수정렬','주사위 세개','개수세기','스타트링크',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',
                  '//*[@id="web_2"]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[4]/div[1]/a',#34
                  '//*[@id="web_1"]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[4]/div[1]/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',
                  '//*[@id="web_2"]/div/a',
                  '//*[@id="web_1"]/div/a',#39
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',
                  '//*[@id="web_3"]/div/a',#41'줄세우기','문자열폭발','군계일학','소수구하기','이상한기호',
                  '//*[@id="web_3"]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div[1]/a',#44
                  '//*[@id="web_1"]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a'#46,'casio','babba','01','돌게임6','랜덤'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#49
                  '//*[@id="web_2"]/div/a',#50'삼각형','카카오','상금','sort','밑줄','부분수열','부분집합','시험감독','2차원','보물'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',
                  '//*[@id="web_1"]/div/a',#53
                  '//*[@id="web_3"]/div/a',
                  '//*[@id="web_1"]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div/a',
                  '//*[@id="web_3"]/div/a',#58
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',
                  '//*[@id="web_1"]/div/a',
                  '//*[@id="web_2"]/div/a',#65
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',
                  '//*[@id="web_1"]/div/a'][k]
            sleep(uniform(0.5, 1.5))
            browser.find_element_by_xpath(path).click()
            sleep(uniform(0.5, 1.5))
        
            #top=500;bottom=randint(100,1000)
            #browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
            #sleep(uniform(0.5, 1.5))
            if i==3:break
    except:pass

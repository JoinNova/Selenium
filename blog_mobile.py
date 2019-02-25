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
            path=['//*[@id="web_3"]/div/a',#01난제
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#02행운의편지
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div[1]/a',#03if
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#04비슷한단어
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#05super
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#06strange',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',#07'quarters',
                  '//*[@id="web_1"]/div/a',#08'지각',
                  '//*[@id="web_2"]/div/a',#09'N과M'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',#10,'골드바흐
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',#11'타일링','
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#12'피터팬',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div[1]/a',#13'Z',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',#14'청기','
                  '//*[@id="web_2"]/div/a',#15만취한',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',#16'gcd','
                  '//*[@id="web_3"]/div/a',#17탈출','
                  '//*[@id="web_1"]/div/a',#18역배치',
                  '//*[@id="web_1"]/div/a',#19'스테판'
                  '//*[@id="web_1"]/div/a',#20,'한조
                  '//*[@id="web_1"]/div/a',#21'key',
                  '//*[@id="web_1"]/div/a',#22'부분합','
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div/a',#23숨바꼭질'
                  '//*[@id="web_2"]/div/a',#24','dslr'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',#25,'팰린드롬
                  '//*[@id="web_1"]/div/a',#26','수묶기'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#27,'회의실배정'
                  '//*[@id="web_1"]/div/a',#28,'부분문자열',
                  '//*[@id="web_1"]/div/a',#29'contest'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',#30,'시간초과',
                  '//*[@id="web_2"]/div/a',#31탑',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#32'쇠막대기'
                  '//*[@id="web_2"]/div/a',#33,'엄청난'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div[1]/a',#34,'정렬',
                  '//*[@id="web_1"]/div/a',#35'중복'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[4]/div[1]/a',#36,'좌표',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',#37'수정렬',
                  '//*[@id="web_2"]/div/a',#38'주사위 세개','
                  '//*[@id="web_1"]/div/a',#39개수세기',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#40'스타트링크',
                  '//*[@id="web_3"]/div/a',#41'줄세우기',
                  '//*[@id="web_3"]/div/a',#42'문자열폭발'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',#43,'군계일학',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[4]/div[1]/a',#44'소수구하기'
                  '//*[@id="web_1"]/div/a',#45,'이상한기호',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',#46'casio'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',#47,'babba'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',#48,'01',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div/a',#49'돌게임6'
                  '//*[@id="web_2"]/div/a',#50,'랜덤'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',#51'삼각형'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[1]/div[1]/a',#52,'카카오''
                  '//*[@id="web_1"]/div/a',#53,'상금',
                  '//*[@id="web_3"]/div/a',#54'sort',
                  '//*[@id="web_1"]/div/a',#55'밑줄'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div/a',#56,'부분수열'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[3]/div/a',#57,'부분집합',
                  '//*[@id="web_3"]/div/a',#58'시험감독'
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',#59,'2차원',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',#60'보물
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li[2]/div[1]/a',#61'암호',
                  '//*[@id="web_1"]/div/a',#62'이상한',
                  '//*[@id="web_2"]/div/a',#63'연세대학교',
                  '//*[@id="_ugc_review_html"]/div/div[2]/panel-list/div[1]/panel-list/div/select-contents/div/ul/li/div/a',#64'신용카드'
                  '//*[@id="web_1"]/div/a'][k]#65,'입실'
            print(k,sr,'\n',path)
            sleep(uniform(0.5, 1.5))
            browser.find_element_by_xpath(path).click()
            sleep(uniform(0.5, 1.5))
        
            #top=500;bottom=randint(100,1000)
            #browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
            #sleep(uniform(0.5, 1.5))
            if i==3:break
    except:pass

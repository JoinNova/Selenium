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
            browser.get('https://m.daum.net/')
            sleep(uniform(1.0, 1.5))
            k=randint(0,64)
            sr = "백준 알고리즘 "+['난제','행운의편지','if','비슷한단어','super','strange','quarters','지각','N과M','골드바흐',
                             '타일링','피터팬','Z boj1074','청기','만취한','gcd','탈출','역배치','스테판','한조',
                             'key','부분합','숨바꼭질 boj','dslr','팰린드롬','수묶기','회의실배정','부분문자열','contest','시간초과',
                             '탑','쇠막대기 boj','엄청난','정렬 boj','중복 boj','좌표 boj','linear','주사위 세개','개수세기','스타트링크 boj',
                             '줄세우기','문자열폭발','군계일학','소수구하기 boj','이상한기호','casio','babba','01','돌게임6','랜덤',
                             '삼각형','카카오','상금','sort','밑줄','부분수열','부분집합 boj','시험감독','2차원 배열 boj','보물',
                             '암호','이상한','연세대학교','신용카드','입실'][k]
            #PW = "사용자비밀번호"
            elem_search = browser.find_element_by_name("q")
            elem_search.send_keys(sr)
            browser.find_element_by_xpath('//*[@id="form_totalsearch"]/fieldset/div/div/button[2]').click()
            #elem_login = browser.find_element_by_name("login_password")
            #elem_login.send_keys(PW)
            sleep(uniform(0.5, 1.5))
            path=['//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#01난제
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',#02행운의편지
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#03if
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#04비슷한단어
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#05super
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#06strange',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#07'quarters',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#08'지각',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#09'N과M'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#10,'골드바흐
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#11'타일링','
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#12'피터팬',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#13'Z boj1074',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#14'청기','
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#15만취한',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#16'gcd','
                  '//*[@id="totalWebColl"]/div[2]/ul/li[5]/a',#17탈출','
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',#18역배치',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#19'스테판'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#20,'한조
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#21'key',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',#22'부분합','
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#23숨바꼭질 boj'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#24','dslr'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#25,'팰린드롬
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#26','수묶기'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#27,'회의실배정'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',#28,'부분문자열',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#29'contest'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#30,'시간초과',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#31탑',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#32'쇠막대기 boj'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',#33,'엄청난'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#34,'정렬 boj',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#35'중복 boj'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#36,'좌표 boj',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#37'수정렬',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#38'주사위 세개','
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#39개수세기',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#40'스타트링크 boj',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#41'줄세우기',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',#42'문자열폭발'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#43,'군계일학',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#44'소수구하기 boj'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#45,'이상한기호',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#46'casio'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#47,'babba'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[3]/a',#48,'01',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#49'돌게임6'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#50,'랜덤'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#51'삼각형'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#52,'카카오''
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#53,'상금',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',#54'sort',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#55'밑줄'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#56,'부분수열'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#57,'부분집합 boj',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#58'시험감독'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#59,'2차원 배열 boj',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#60'보물
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',#61'암호',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',#62'이상한',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#63'연세대학교',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',#64'신용카드'
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a'][k]#65,'입실'
            print(k,sr,'\n',path)
            sleep(uniform(0.5, 1.5))
            browser.find_element_by_xpath(path).click()
            sleep(uniform(0.5, 1.5))
        
            #top=500;bottom=randint(100,1000)
            #browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
            #sleep(uniform(0.5, 1.5))
            if i==3:break
    except:pass


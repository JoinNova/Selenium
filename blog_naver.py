from time import sleep
from selenium import webdriver
from random import *
from selenium import webdriver

key=-1
k=-1
while 1:
    try:
        browser = webdriver.Chrome(executable_path = '/Users/nova/git/chromedriver')
        #browser = webdriver.Firefox(executable_path = '/Users/nova/git/webdriver/geckodriver')
        browser.set_window_size(1280, 360)
        i=0
        while 1:
            i+=1
            browser.get('https://www.naver.com/')
            sleep(uniform(1.0, 1.5))
            way=randint(5,5)
            if way==0 or way==1 or way==2:
                key=randint(0,5)
                sr=['2019 제1회 정보처리기사 합격 실기','2019 제1회 정보처리기사 합격 실기',
                    '2019 제1회 정보처리기사 합격 실기','리눅스마스터 합격자발표',
                    '리눅스마스터 2급 2차 A형','리눅스마스터 2급 2차 A형'][key]
                path=['//*[@id="sp_blog_3"]/dl/dt/a','//*[@id="sp_blog_3"]/dl/dt/a',
                      '//*[@id="sp_blog_3"]/dl/dt/a','//*[@id="sp_blog_1"]/dl/dt/a',
                      '//*[@id="sp_blog_3"]/dl/dt/a','//*[@id="sp_blog_3"]/dl/dt/a'][key]
            elif way==4 or way==3:
                key=randint(0,29)
                #key+=1
                sr=['정보처리기사 실기 정렬','정보처리기사 실기 버블정렬','정보처리기사 실기 급여계산','정보처리기사 실기 재고관리','정보처리기사 실기 통계산출',
                    '정보처리기사 실기 최소비용','정보처리기사 실기 이분탐색','정보처리기사 실기 병합정렬','정보처리기사 실기 퀵정렬','정보처리기사 실기 석차구하기',
                    '정보처리기사 실기 배열','정보처리기사 실기 행렬','정보처리기사 실기 마름모','정보처리기사 실기 달팽이','정보처리기사 실기 패리티',
                    '정보처리기사 실기 BCD','정보처리기사 실기 2진수','정보처리기사 실기 16진수','정보처리기사 실기 1의보수','정보처리기사 실기 최대공약수',
                    '정보처리기사 실기 기출문제','정보처리기사 실기 기출문제 2019 제3회','정보처리기사 실기 기출문제 2019 제2회','정보처리기사 실기 기출문제 2019 제1회',
                    '정보처리기사 실기 기출문제 2018 제1회','정보처리기사 실기 기출문제 2018 제2회','정보처리기사 실기 기출문제 2018 제3회','정보처리기사 실기 기출문제 2017 제3회',
                    '정보처리기사 실기 기출문제 2017 제2회','정보처리기사 실기 기출문제 2017 제1회',''][key]
                path=['//*[@id="sp_blog_2"]/dl/dt/a',#01 정렬
                      '//*[@id="sp_blog_2"]/dl/dt/a',#02 버블정렬
                      '//*[@id="sp_blog_1"]/dl/dt/a',#03 급여계싼
                      '//*[@id="sp_blog_1"]/dl/dt/a',#04재고관리
                      '//*[@id="sp_blog_1"]/dl/dt/a',#05통계산출
                      '//*[@id="sp_blog_1"]/dl/dt/a',#06최소비용
                      '//*[@id="sp_blog_1"]/dl/dt/a',#07이분탐색
                      '//*[@id="sp_blog_1"]/dl/dt/a',#08병합정렬
                      '//*[@id="sp_blog_1"]/dl/dt/a',#09퀵정렬
                      '//*[@id="sp_blog_1"]/dl/dt/a',#10석차구하기
                      '//*[@id="sp_blog_3"]/dl/dt/a',#11배열######
                      '//*[@id="sp_blog_1"]/dl/dt/a',#12행렬
                      '//*[@id="sp_blog_1"]/dl/dt/a',#13마름모
                      '//*[@id="sp_blog_2"]/dl/dt/a',#14달팽이
                      '//*[@id="sp_blog_1"]/dl/dt/a',#15패리티
                      '//*[@id="sp_blog_1"]/dl/dt/a',#16BCD
                      '//*[@id="sp_blog_1"]/dl/dt/a',#172진수
                      '//*[@id="sp_blog_1"]/dl/dt/a',#1816진수
                      '//*[@id="sp_blog_3"]/dl/dt/a',#191의보수
                      '//*[@id="sp_blog_3"]/dl/dt/a',#20최대공약수###
                      '//*[@id="sp_blog_4"]/dl/dt/a',
                      '//*[@id="sp_blog_2"]/dl/dt/a',
                      '//*[@id="sp_blog_2"]/dl/dt/a',
                      '//*[@id="sp_blog_2"]/dl/dt/a',
                      '//*[@id="sp_blog_1"]/dl/dt/a',
                      '//*[@id="sp_blog_1"]/dl/dt/a',
                      '//*[@id="sp_blog_1"]/dl/dt/a',
                      '//*[@id="sp_blog_1"]/dl/dt/a',
                      '//*[@id="sp_blog_2"]/dl/dt/a',
                      '//*[@id="sp_blog_2"]/dl/dt/a'][key]
            else:
                #k=randint(0,79)
                k+=1
                sr = "백준 알고리즘 "+['난제','행운의편지','if boj','비슷한단어','super','strange','quarters','지각','N과M','골드바흐',
                                 '타일링','피터팬','Z','청기','만취한','gcd','탈출','역배치','스테판','한조',
                                 'key','부분합','숨바꼭질','dslr','팰린드롬','수묶기','회의실배정','부분문자열','contest','시간초과',
                                 '탑','쇠막대기','엄청난','정렬','중복','좌표','수정렬','주사위 boj','개수세기','스타트링크',
                                 '줄세우기 boj','문자열폭발','군계일학','소수 boj','이상한기호','casio','babba','01','돌게임 boj','랜덤',
                                 '삼각형','카카오','상금','sort','밑줄','부분수열','부분집합','시험 boj','2차원','보물',
                                 '암호 boj','이상한','연세대학교','신용카드','입실','나머지합','피보나치','factorial','계단 boj','description',
                                 '동전 boj','암호제작','adding','공백','암호코드','버블 boj','이진트리','winning','별 boj','are'][k]
                #PW = "사용자비밀번호"
            elem_search = browser.find_element_by_name("query")
            elem_search.send_keys(sr)
            browser.find_element_by_xpath('//*[@id="search_btn"]').click()
            #elem_login = browser.find_element_by_name("login_password")
            #elem_login.send_keys(PW)
            sleep(uniform(0.5, 1.2))
            if  way==5:
                path=['//*[@id="web_layer_2"]/dl/dt/a',#01난제
                      '//*[@id="sp_blog_1"]/dl/dt/a',#02행운의편지
                      '//*[@id="web_layer_0"]/dl/dt/a',#03if boj
                      '//*[@id="web_layer_0"]/dl/dt/a',#04비슷한단어
                      '//*[@id="sp_blog_1"]/dl/dt/a',#05super
                      '//*[@id="web_layer_0"]/dl/dt/a',#06strange',
                      '//*[@id="sp_blog_1"]/dl/dt/a',#07'quarters',
                      '//*[@id="web_layer_0"]/dl/dt/a',#08'지각',
                      '//*[@id="web_layer_1"]/dl/dt/a',#09'N과M'###
                      '//*[@id="sp_blog_4"]/dl/dt/a',#10,'골드바흐
                      '//*[@id="sp_blog_1"]/dl/dt/a',#11'타일링','
                      '//*[@id="web_layer_0"]/dl/dt/a',#12'피터팬',
                      '//*[@id="sp_blog_3"]/dl/dt/a',#13'Z'###
                      '//*[@id="sp_blog_1"]/dl/dt/a',#14'청기','
                      '//*[@id="web_layer_0"]/dl/dt/a',#15만취한',
                      '//*[@id="sp_blog_1"]/dl/dt/a',#16'gcd','
                      '//*[@id="sp_blog_4"]/dl/dt/a',#17탈출','
                      '//*[@id="web_layer_0"]/dl/dt/a',#18역배치',
                      '//*[@id="web_layer_0"]/dl/dt/a',#19'스테판'
                      '//*[@id="web_layer_0"]/dl/dt/a',#20,'한조
                      '//*[@id="web_layer_0"]/dl/dt/a',#21'key',
                      '//*[@id="web_layer_0"]/dl/dt/a',#22'부분합','
                      '//*[@id="sp_blog_5"]/dl/dt/a',#23숨바꼭질'
                      '//*[@id="web_layer_0"]/dl/dt/a',#24','dslr'
                      '//*[@id="sp_blog_2"]/dl/dt/a',#25,'팰린드롬
                      '//*[@id="web_layer_0"]/dl/dt/a',#26','수묶기'
                      '//*[@id="sp_blog_4"]/dl/dt/a',#27,'회의실배정'
                      '//*[@id="web_layer_0"]/dl/dt/a',#28,'부분문자열',
                      '//*[@id="web_layer_0"]/dl/dt/a',#29'contest'
                      '//*[@id="web_layer_0"]/dl/dt/a',#30,'시간초과',
                      '//*[@id="sp_blog_2"]/dl/dt/a',#31탑',###
                      '//*[@id="sp_blog_4"]/dl/dt/a',#32'쇠막대기'
                      '//*[@id="web_layer_0"]/dl/dt/a',#33,'엄청난'
                      '//*[@id="sp_blog_4"]/dl/dt/a',#34,'정렬',
                      '//*[@id="web_layer_0"]/dl/dt/a',#35'중복'
                      '//*[@id="sp_blog_5"]/dl/dt/a',#36,'좌표',
                      '//*[@id="sp_blog_2"]/dl/dt/a',#37'수정렬',
                      '//*[@id="sp_blog_1"]/dl/dt/a',#38'주사위 boj','
                      '//*[@id="web_layer_0"]/dl/dt/a',#39개수세기',
                      '//*[@id="sp_blog_1"]/dl/dt/a',#40'스타트링크',
                      '//*[@id="web_layer_0"]/dl/dt/a',#41'줄세우기',
                      '//*[@id="web_layer_1"]/dl/dt/a',#42'문자열폭발'####
                      '//*[@id="sp_blog_1"]/dl/dt/a',#43,'군계일학',
                      '//*[@id="web_layer_0"]/dl/dt/a',#44'소수boj'
                      '//*[@id="web_layer_0"]/dl/dt/a',#45,'이상한기호',
                      '//*[@id="sp_blog_1"]/dl/dt/a',#46'casio'
                      '//*[@id="sp_blog_1"]/dl/dt/a',#47,'babba'
                      '//*[@id="sp_blog_2"]/dl/dt/a',#48,'01',####
                      '//*[@id="sp_blog_1"]/dl/dt/a',#49'돌게임6'
                      '//*[@id="web_layer_0"]/dl/dt/a',#50,'랜덤'
                      '//*[@id="sp_blog_2"]/dl/dt/a',#51'삼각형'####
                      '//*[@id="sp_blog_1"]/dl/dt/a',#52,'카카오''
                      '//*[@id="web_layer_0"]/dl/dt/a',#53,'상금',
                      '//*[@id="sp_blog_2"]/dl/dt/a',#54'sort',####
                      '//*[@id="web_layer_0"]/dl/dt/a',#55'밑줄'
                      '//*[@id="sp_blog_3"]/dl/dt/a',#56,'부분수열'
                      '//*[@id="sp_blog_4"]/dl/dt/a',#57,'부분집합',
                      '//*[@id="sp_blog_1"]/dl/dt/a',#58'시험 boj'###
                      '//*[@id="sp_blog_3"]/dl/dt/a',#59,'2차원',
                      '//*[@id="sp_blog_3"]/dl/dt/a',#60'보물
                      '//*[@id="sp_blog_1"]/dl/dt/a',#61'암호'boj
                      '//*[@id="web_layer_0"]/dl/dt/a',#62'이상한',
                      '//*[@id="web_layer_0"]/dl/dt/a',#63'연세대학교',
                      '//*[@id="sp_blog_1"]/dl/dt/a',#64'신용카드'
                      '//*[@id="web_layer_0"]/dl/dt/a',#65,'입실'
                      '//*[@id="web_layer_0"]/dl/dt/a',#66 나머지합
                      '//*[@id="sp_blog_5"]/dl/dt/a',#67피보나치
                      '//*[@id="sp_blog_2"]/dl/dt/a',#68factorial####
                      '//*[@id="web_layer_0"]/dl/dt/a',#69계단 boj
                      '//*[@id="web_layer_0"]/dl/dt/a',#70description
                      '//*[@id="sp_blog_1"]/dl/dt/a',#71 동전 boj
                      '//*[@id="sp_blog_1"]/dl/dt/a',#72암호제작
                      '//*[@id="web_layer_0"]/dl/dt/a',#73 adding
                      '//*[@id="web_layer_0"]/dl/dt/a',#74 공백
                      '//*[@id="sp_blog_1"]/dl/dt/a',#75 암호코드
                      '//*[@id="web_layer_0"]/dl/dt/a',#76 버블 boj
                      '//*[@id="sp_blog_1"]/dl/dt/a',#77이진트리
                      '//*[@id="sp_blog_1"]/dl/dt/a',#78winning
                      '//*[@id="sp_blog_1"]/dl/dt/a',#79별boj
                      '//*[@id="web_layer_0"]/dl/dt/a',#80are
                      ''][k]
            print(k,key,sr,'\n',path)
            #sleep(uniform(0.5, 1.2))
            browser.find_element_by_xpath(path).click()
            '''
            cli=randint(0,100)
            if cli!=50: #or cli==60 or cli==70:
                num=['','','','','','','','']
                for _ in path:
                    if 
                browser.get(path)
                sleep(uniform(2.5, 4.5))
                path=['','','','','',
                      '//*[@id="sf_align"]/div/div/dl/dt[1]/a',
                      '//*[@id="sf_align"]/div/div/dl/dt[2]/a',
                      '//*[@id="sf_align"]/div/div/dl/dt[3]/a',
                      '','',''][cli//10]
                browser.find_element_by_xpath(path).click()
                print('Click\n',path)
                sleep(uniform(0.5, 1.7))
            else:
                sleep(uniform(0.5, 1.2))'''
            sleep(uniform(0.5, 1.2))
            #top=500;bottom=randint(100,1000)
            #browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
            #sleep(uniform(0.5, 1.5))
            if i==2:break
    except:pass

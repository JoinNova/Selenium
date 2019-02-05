from time import sleep
from selenium import webdriver
from random import *
while 1:
    browser = webdriver.Chrome(executable_path=r"/Users/nova/git/chromedriver")
    browser.set_window_size(960, 800)
    i=0
    root=randint(0,1)
    if root==0:
        while 1:
            i+=1
            browser.get('https://www.naver.com/')
            sleep(uniform(1.0, 1.5))
            sub=randint(1,3)
            if sub==0:
                k=randint(0,39)
                sr = "백준알고리즘 "+['소수','피보나치','난제','스타트링크','별 찍기','정렬','신용카드','문자열','팰린드롬','대소문자',
                                '크로스워드','8진수','카이사르','명령프롬프트','단어길이','골드바흐','감소하는수','랜덤','boj2839','다이나믹',
                                '10993','10996','일반화학실험','12096','Doubles','파일완전삭제','네자리','마리오','ㅊ멘','fro',
                                '보물','2의제곱','더하기3','rot','아','암호','좋아해','누울','저작권','소수찾기'][k]
                #PW = "사용자비밀번호"
                elem_search = browser.find_element_by_name("query")
                elem_search.send_keys(sr)

                #elem_login = browser.find_element_by_name("login_password")
                #elem_login.send_keys(PW)
                sleep(uniform(1.0, 2.5))
                browser.find_element_by_xpath('//*[@id="search_btn"]').click()
                path1=['//*[@id="sp_blog_4"]/dl/dd[3]/span/a[2]','//*[@id="sp_blog_4"]/dl/dd[3]/span/a[2]','//*[@id="web_layer_2"]/dl/dd[1]/div/a',
                      '//*[@id="sp_blog_1"]/dl/dd[3]/span/a[2]','//*[@id="sp_blog_4"]/dl/dd[3]/span/a[2]','//*[@id="sp_blog_3"]/dl/dt/a',
                      '//*[@id="sp_blog_1"]/dl/dd[3]/span/a[2]','//*[@id="sp_blog_3"]/dl/dd[3]/span/a[2]','//*[@id="sp_blog_2"]/dl/dd[3]/span/a[2]',
                      '//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="sp_blog_2"]/dl/dd[3]/span/a[2]',
                      '//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="sp_blog_2"]/dl/dd[3]/span/a[2]','//*[@id="sp_blog_3"]/dl/dd[3]/span/a[2]',
                      '//*[@id="sp_blog_3"]/dl/dd[3]/span/a[2]','//*[@id="web_layer_1"]/dl/dd[1]/div/a','//*[@id="sp_blog_3"]/dl/dt/a',
                      '//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="sp_blog_1"]/dl/dt/a','//*[@id="web_layer_0"]/dl/dd[1]/div/a',
                      '//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="sp_blog_1"]/dl/dd[3]/span/a[2]','//*[@id="sp_blog_1"]/dl/dd[3]/span/a[2]',
                      '//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="web_layer_0"]/dl/dd[1]/div/a',
                      '//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="sp_blog_1"]/dl/dt/a','//*[@id="web_layer_0"]/dl/dd[1]/div/a',
                      '//*[@id="web_layer_2"]/dl/dd[1]/div/a','//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="sp_blog_2"]/dl/dd[3]/span/a[2]',
                      '//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="sp_blog_3"]/dl/dt/a',
                      '//*[@id="web_layer_0"]/dl/dd[1]/div/a','//*[@id="sp_blog_2"]/dl/dd[3]/span/a[2]','//*[@id="web_layer_1"]/dl/dd[1]/div/a',
                      '//*[@id="sp_blog_5"]/dl/dt/a'][k]
                sleep(uniform(0.5, 2.5))
                browser.find_element_by_xpath(path1).click()
                sleep(uniform(0.5, 2.5))
                
                top=500;bottom=randint(100,1000)
                browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
                sleep(uniform(0.5, 1.5))
                if i==10:break
            elif sub==1:
                k=randint(0,11)
                sr = "우분투 "+['빅데이터','윈도우','한글','맥북','mysql','듀얼부팅','부팅 usb 세팅','mac 듀얼','18.04 usb yumi','부팅','인스타 크롤링','크롤링'][k]
                #PW = "사용자비밀번호"
                elem_search = browser.find_element_by_name("query")
                elem_search.send_keys(sr)

                #elem_login = browser.find_element_by_name("login_password")
                #elem_login.send_keys(PW)
                sleep(uniform(1.0, 2.5))
                browser.find_element_by_xpath('//*[@id="search_btn"]').click()
                path1=['//*[@id="sp_blog_3"]/div/a/img','//*[@id="sp_blog_2"]/div/a/img','//*[@id="sp_blog_5"]/div/a/img','//*[@id="sp_blog_1"]/dl/dt/a','//*[@id="sp_blog_5"]/div/a/img',
                       '//*[@id="sp_blog_2"]/div/a/img','//*[@id="sp_blog_2"]/div/a/img','//*[@id="sp_blog_1"]/dl/dt/a','//*[@id="web_layer_1"]/dl/dt/a','//*[@id="sp_blog_3"]/dl/dt/a',
                       '//*[@id="sp_blog_1"]/div/a/img','//*[@id="sp_blog_1"]/div/a/img'][k]
                sleep(uniform(0.5, 2.5))
                browser.find_element_by_xpath(path1).click()
                sleep(uniform(0.5, 2.5))
                
                top=500;bottom=randint(100,1000)
                browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
                sleep(uniform(0.5, 1.5))
                if i==10:break
            elif sub==2:
                k=randint(0,9)
                sr = "크롤링 "+['인스타','insta','셀레니움 인스타','쿠팡','아파치','tripadvisor','coupang','우분투','우분투 파이썬','파이썬 우분투'][k]
                #PW = "사용자비밀번호"
                elem_search = browser.find_element_by_name("query")
                elem_search.send_keys(sr)

                #elem_login = browser.find_element_by_name("login_password")
                #elem_login.send_keys(PW)
                sleep(uniform(1.0, 2.5))
                browser.find_element_by_xpath('//*[@id="search_btn"]').click()
                path1=['//*[@id="sp_blog_3"]/div/a/img','//*[@id="sp_blog_1"]/div/a/img','//*[@id="web_layer_1"]/dl/dt/a','//*[@id="sp_blog_1"]/div/a/img','//*[@id="web_layer_0"]/dl/dt/a',
                       '//*[@id="web_layer_0"]/dl/dt/a','//*[@id="web_layer_0"]/dl/dt/a','//*[@id="sp_blog_1"]/div/a/img','//*[@id="sp_blog_2"]/dl/dt/a','//*[@id="sp_blog_2"]/div/a/img'][k]
                sleep(uniform(0.5, 2.5))
                browser.find_element_by_xpath(path1).click()
                sleep(uniform(0.5, 2.5))
                
                top=500;bottom=randint(100,1000)
                browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
                sleep(uniform(0.5, 1.5))
                if i==10:break
            elif sub==3:
                k=randint(0,9)
                sr = "hackerrank "+['findall','mutation','Linked Lists','Binary Search Trees','BST Level-Order Traversal',
                                    'Exceptions','Queues and Stacks','2D Arrays','Class vs. Instance','Find Digits'][k]
                #PW = "사용자비밀번호"
                elem_search = browser.find_element_by_name("query")
                elem_search.send_keys(sr)

                #elem_login = browser.find_element_by_name("login_password")
                #elem_login.send_keys(PW)
                sleep(uniform(1.0, 2.5))
                browser.find_element_by_xpath('//*[@id="search_btn"]').click()
                path1=['//*[@id="sp_blog_1"]/dl/dt/a','//*[@id="sp_blog_1"]/dl/dt/a','//*[@id="sp_blog_2"]/dl/dt/a','//*[@id="sp_blog_2"]/dl/dt/a','//*[@id="sp_blog_1"]/dl/dt/a',
                       '//*[@id="sp_blog_1"]/dl/dt/a','//*[@id="sp_blog_1"]/dl/dt/a','//*[@id="sp_blog_2"]/dl/dt/a','//*[@id="sp_blog_1"]/dl/dt/a','//*[@id="sp_blog_1"]/dl/dt/a'][k]
                sleep(uniform(0.5, 2.5))
                browser.find_element_by_xpath(path1).click()
                sleep(uniform(0.5, 2.5))
                
                top=500;bottom=randint(100,1000)
                browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
                sleep(uniform(0.5, 1.5))
                if i==10:break
                

    elif root==1:
        while 1:
            i+=1
            browser.get('https://www.daum.net/')
            sleep(uniform(0.5, 2.5))
            k=randint(0,11)
            sr = "백준알고리즘 "+['boj10943','난제','신용카드','문자열폭발','팰린드롬 boj10235','대소문자',
                            '카이사르5598','골드바흐의 추측 boj 9020','감소하는수','랜덤','10993','일반화학실험'][k]
            #PW = "사용자비밀번호"
            elem_search = browser.find_element_by_name("q")
            elem_search.send_keys(sr)

            #elem_login = browser.find_element_by_name("login_password")
            #elem_login.send_keys(PW)
            sleep(uniform(0.5, 2.5))
            browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]').click()
            path=['//*[@id="blogColl"]/div[2]/ul/li[2]/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[1]/div[1]/div/a',
                  '//*[@id="blogColl"]/div[2]/ul/li[1]/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[2]/div[1]/div/a',
                  '//*[@id="blogColl"]/div[2]/ul/li[2]/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[1]/div[1]/div/a',
                  '//*[@id="blogColl"]/div[2]/ul/li[2]/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[3]/div[1]/div/a',
                  '//*[@id="blogColl"]/div[2]/ul/li[2]/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[1]/div[1]/div/a',
                  '//*[@id="blogColl"]/div[2]/ul/li/div[1]/div/a','//*[@id="blogColl"]/div[2]/ul/li[1]/div[1]/div/a'][k]
            sleep(uniform(0.5, 2.5))
            browser.find_element_by_xpath(path).click()
            sleep(uniform(0.5, 2.5))
            
            top=500;bottom=randint(100,1000)
            browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
            sleep(uniform(1.0, 1.5))
            if i==10:break


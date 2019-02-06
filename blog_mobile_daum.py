from time import sleep
from selenium import webdriver
from random import *
from selenium import webdriver


while 1:
    try:
        browser = webdriver.Chrome(executable_path=r"/home/nova/git/chromedriver")
        browser.set_window_size(375, 812)
        i=0
        while 1:
            i+=1
            browser.get('https://m.daum.net/')
            sleep(uniform(0.5, 2.0))
            k=randint(0,40)
            sr = "hackerrank "+['Linked Lists','BST','MAXMIN','Binary Search','Generic',
                                'sorting','Interface','Queues','Exceptions','String to',
                                'Linked','WorkBook','Chocolate','Fibo','Digit',
                                'Sherlock','Append','Extra','Scope','Abstract',
                                'Characters','Strong Password_','Camelcase','Reduced','Inheritance',
                                '2D Arrays','Binary Numbers','Recursion','Dictionaries','Day 7',
                                "Let's",'instance','loops','conditional','operators',
                                'Arrays DS','Hello World','Array ds','Jumping','Repeat','Torsional'][k]
            #PW = "사용자비밀번호"
            elem_search = browser.find_element_by_name("q")
            elem_search.send_keys(sr)
            browser.find_element_by_xpath('//*[@id="form_totalsearch"]/fieldset/div[2]/div/button[2]/span').click()
            #elem_login = browser.find_element_by_name("login_password")
            #elem_login.send_keys(PW)
            sleep(uniform(0.5, 2.0))
            path=['//*[@id="totalWebColl"]/div[2]/ul/li[1]/a','//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a','//*[@id="totalWebColl"]/div[2]/ul/li[5]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[5]/a','//*[@id="totalWebColl"]/div[2]/ul/li[8]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[7]/a','//*[@id="totalWebColl"]/div[2]/ul/li[6]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a','//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[4]/a','//*[@id="totalWebColl"]/div[2]/ul/li[6]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[4]/a','//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[7]/a','//*[@id="totalWebColl"]/div[2]/ul/li[10]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a','//*[@id="totalWebColl"]/div[2]/ul/li[5]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[3]/a','//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[3]/a','//*[@id="totalWebColl"]/div[2]/ul/li[6]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[6]/a','//*[@id="totalWebColl"]/div[2]/ul/li[5]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[3]/a','//*[@id="totalWebColl"]/div[2]/ul/li[2]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a','//*[@id="totalWebColl"]/div[2]/ul/li[5]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a','//*[@id="totalWebColl"]/div[2]/ul/li[4]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a','//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[1]/a','//*[@id="totalWebColl"]/div[2]/ul/li[5]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[2]/a','//*[@id="totalWebColl"]/div[2]/ul/li[3]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[3]/a','//*[@id="totalWebColl"]/div[2]/ul/li[5]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li[5]/a','//*[@id="totalWebColl"]/div[2]/ul/li[1]/a',
                  '//*[@id="totalWebColl"]/div[2]/ul/li/a'][k]
            sleep(uniform(0.5, 2.0))
            browser.find_element_by_xpath(path).click()
            sleep(uniform(0.5, 2.0))
            
            #top=500;bottom=randint(100,1000)
            #browser.execute_script("window.scrollTo(%d, %d)"%(top,bottom))
            #sleep(uniform(0.5, 1.5))
            if i==1:break
    except:print(sr);pass

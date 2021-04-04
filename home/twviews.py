from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
import time
def homes(request):
    return render(request,'twitter.html')
def twitters(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://twitter.com/login')
    time.sleep(5)
    print("done")

    def login():
        time.sleep(2)
        global tags
        tname=request.POST["tname"]
        tpass=request.POST["tpass"]
        tags=request.POST["tags"]
        time.sleep(2)
        login = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
        login.send_keys(tname)
        password = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")
        password.send_keys(tpass)
        time.sleep(2)

        driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div").click()
        time.sleep(3)
        print("yes")

    login()

    # hastag in search
    def search():
        time.sleep(2)
        searchhastag = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchhastag.send_keys(tags)
        searchhastag.submit()
        time.sleep(2)

        time.sleep(5)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a").click()
        time.sleep(3)

    search()

    global user_profile
    global url, url2, url3

    def scroll():
        global user_profile
        global url, url2, url3
        driver.current_url
        time.sleep(2)
        for i in range(1, 5):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(5)
        url = driver.current_url
        driver.current_url
        time.sleep(5)
        tweets = driver.find_elements_by_tag_name('a')
        user_profile = [elem.get_attribute('href') for elem in tweets]
        print("first me")

    def scroll2():
        global url, url2, url3
        global user_profile
        driver.get(url)
        time.sleep(5)
        for i in range(1, 5):
            driver.execute_script("window.scrollTo(3000,document.body.scrollHeight)")
            time.sleep(5)
        url2 = driver.current_url
        driver.current_url
        time.sleep(5)
        tweets = driver.find_elements_by_tag_name('a')
        user_profile = [elem.get_attribute('href') for elem in tweets]
        print("Second me")

    def scroll3():
        global url, url2, url3
        global user_profile
        driver.get(url2)
        time.sleep(5)
        for i in range(1, 5):
            driver.execute_script("window.scrollTo(6000,document.body.scrollHeight)")
            time.sleep(5)
        url2 = driver.current_url
        driver.current_url
        time.sleep(5)
        tweets = driver.find_elements_by_tag_name('a')
        user_profile = [elem.get_attribute('href') for elem in tweets]
        print("third me")

    def scroll4():
        global url, url2, url3
        global user_profile

        driver.get(url2)
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(10000,document.body.scrollHeight)")
            time.sleep(5)
        url3 = driver.current_url
        driver.current_url
        time.sleep(5)
        tweets = driver.find_elements_by_tag_name('a')
        user_profile = [elem.get_attribute('href') for elem in tweets]
        print("fourth me")

    # link filtering
    def likes():
        time.sleep(5)
        a = set(user_profile)
        time.sleep(2)
        users = list(a)
        a = []
        time.sleep(10)
        for link in users:
            if len(link) <= 35:
                a.append(link)
        c = set(a)
        user = list(c)
        time.sleep(10)
        b = ['https://twitter.com/messages', 'https://twitter.com/compose/tweet', 'https://twitter.com/home',
             'https://twitter.com/explore',
             'https://twitter.com/privacy', 'https://twitter.com/home', 'https://twitter.com/notifications',
             'https://twitter.com/owaish80038333', 'https://t.co/xGHL2hoivI?amp=1']

        for i in b:
            if i in user:
                # print ("found " + i)
                user.remove(i)
                time.sleep(10)
                countdown = random.randint(10, 60)
                time.sleep(countdown)

        for pic_href in user:
            driver.get(pic_href)
            print("done")
            time.sleep(5)
            try:
                # follow user
                time.sleep(2)
                # countdown = random.randint(0,15)
                # time.sleep(countdown)
                time.sleep(3)
                driver.find_element_by_xpath(
                    "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div").click()
                time.sleep(3)
                countdown = random.randint(5, 15)
                time.sleep(countdown)
                print("follow done")
                time.sleep(20)
                # start tweet and like
                # open retweet
                driver.execute("window.scrollTo(0,1500)")
                # get click
                time.sleep(10)
                driver.find_element_by_xpath(
                    "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div").click()
                print("1post done")
                time.sleep(10)
                # open retweet

                # get like
                time.sleep(3)
                driver.find_element_by_xpath(
                    "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div").click()
                print("2post done")
                time.sleep(10)

                # get click
                time.sleep(3)
                driver.find_element_by_xpath(
                    "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[2]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div").click()
                print("3post done")
                time.sleep(20)

            except:
                print("garbage page")
                time.sleep(5)

    time.sleep(5)
    scroll()
    time.sleep(20)
    likes()
    time.sleep(30)
    print("done ist")
    time.sleep(5)
    scroll2()
    time.sleep(25)
    likes()
    time.sleep(30)
    print("done")

    time.sleep(25)
    scroll3()
    time.sleep(20)
    likes()
    time.sleep(30)

    print("2 complet")
    time.sleep(15)
    scroll4()
    time.sleep(29)
    likes()
    time.sleep(30)
    print("like share done")
    return render(request, 'twitter.html')
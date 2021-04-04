from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
import time
def links(request):
    return render(request,'linked.html')

def linkdin(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    time.sleep(2)
    driver.get('https://www.linkedin.com/home')
    time.sleep(5)
    countdown = random.randint(5, 15)
    time.sleep(countdown)
    print("done")

    def login():
        time.sleep(2)
        global ltags
        lemail=request.POST["lemail"]
        lpassw=request.POST["lpassw"]
        ltags=request.POST["ltag"]
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/nav/div/a").click()
        time.sleep(5)
        login = driver.find_element_by_xpath("/html/body/div/main/div[2]/form/div[1]/input")
        login.send_keys(lemail)
        time.sleep(2)
        password = driver.find_element_by_xpath("/html/body/div/main/div[2]/form/div[2]/input")
        password.send_keys(lpassw)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/main/div[2]/form/div[3]/button").click()
        time.sleep(3)
        print("yes")

        countdown = random.randint(5, 15)
        time.sleep(countdown)
    login()

    # hastag in search
    from selenium.webdriver.common.keys import Keys

    time.sleep(10)
    searchhastag = driver.find_element_by_xpath("/html/body/div[7]/header/div[2]/div/div/div[1]/div[1]/input")
    searchhastag.send_keys(ltags)
    searchhastag.send_keys(Keys.ENTER)

    # click follow page
    countdown = random.randint(5, 15)
    time.sleep(countdown)
    time.sleep(5)
    driver.find_element_by_xpath(
        "/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/ul/li[1]/div/div/div[3]/div/button").click()
    time.sleep(3)
    # open follow page
    countdown = random.randint(5, 15)
    time.sleep(countdown)
    time.sleep(5)
    driver.find_element_by_xpath(
        "/html/body/div[7]/div[3]/div/div[2]/div/div[2]/div/div/div/ul/li[1]/div/div/div[2]/a").click()
    time.sleep(3)
    countdown = random.randint(5, 15)
    time.sleep(countdown)
    print("search complete")

    # how to fetch all link
    def fetch():

        for i in range(1, 35):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(7)

        time.sleep(5)
        linkdln = driver.find_elements_by_tag_name('a')
        user_linkedin = [elem.get_attribute('href') for elem in linkdln]
        url = driver.current_url
        driver.current_url
        print("first me")

        time.sleep(5)
        a = set(user_linkedin)
        time.sleep(2)
        users = list(a)
        a = []
        time.sleep(10)
        for link in users:
            if len(link) == 67:
                time.sleep(2)
                a.append(link)
        c = set(a)
        time.sleep(2)
        user = list(c)
        time.sleep(30)
        countdown = random.randint(10, 60)
        time.sleep(countdown)
        print("procces done in fetch all user link")
        print(len(user))
        for pic_href in user:
            driver.get(pic_href)
            time.sleep(10)
            countdown = random.randint(10, 60)
            time.sleep(countdown)
            try:
                # follow user
                time.sleep(2)
                countdown = random.randint(0, 15)
                time.sleep(countdown)
                time.sleep(3)
                driver.find_element_by_xpath(
                    "/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div[2]/div/button").click()
                time.sleep(3)
                print("click done")
                driver.find_element_by_xpath(
                    "/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div/ul/li[4]/div/div").click()
                time.sleep(3)
                print("connect done")

                driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
                time.sleep(5)
                print("add note")
                time.sleep(10)
                countdown = random.randint(0, 15)
                time.sleep(countdown)
                sendmessage = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/textarea")
                sendmessage.send_keys("""Hello,
                I was looking at your profile and I am very impressed with it.
                I would love to connect with you.

                Best regards,
                owaish
                """)
                time.sleep(5)
                countdown = random.randint(5, 10)
                time.sleep(countdown)
                driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
                time.sleep(5)
                print("send message")
            except:
                print("error")
            else:
                print("error")
    fetch()
    print("like share done")
    return render(request, 'linked.html')
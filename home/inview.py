from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
import time
def indexn(request):
    return render(request,'instgram.html')
def insta(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://www.instagram.com/')
    time.sleep(5)
    print("done")
    tag = request.POST["tag"]

    def login():
        time.sleep(2)
        username = request.POST["user"]
        passw = request.POST["pass"]

        login = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        login.send_keys(username)
        password = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password.send_keys(passw)
        time.sleep(2)
        driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()
        time.sleep(3)
        print("yes")
        try:
            # notification
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
            time.sleep(4)
            # driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
            print("done")
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
            print("process complete in try")
        except:
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        else:
            print("error")

    login()

    def search():
        time.sleep(2)
        searchhastag = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        searchhastag.send_keys(tag)
        time.sleep(2)
        driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div/div[1]").click()
        time.sleep(3)

    search()

    def scroll():
        time.sleep(2)
        for i in range(1, 5):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(5)

    def like():
        hastag = "#newyork"
        hrefs = driver.find_elements_by_tag_name('a')
        time.sleep(4)
        pic_href = [elem.get_attribute('href') for elem in hrefs]
        # pic_href =[href for href in pic_href if hastag in href]
        time.sleep(8)
        print(hastag + 'photos' + str(len(pic_href)))

        for pic_href in pic_href:
            driver.get(pic_href)
            print("done")
            time.sleep(5)
            try:
                # follow user
                time.sleep(2)
                countdown = random.randint(0, 15)
                time.sleep(countdown)
                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button").click()
                time.sleep(6)
                countdown = random.randint(0, 15)
                time.sleep(countdown)
                print("follow done")
                # like picture user
                time.sleep(2)
                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[3]/div[2]/div/div/div[1]/div[1]").click()
                time.sleep(2)
                print("done")
                time.sleep(5)
                countdown = random.randint(5, 15)
                time.sleep(countdown)
                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()
                print("like done")
                time.sleep(2)

                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[3]/div[2]/div/div/div[1]/div[2]").click()
                time.sleep(2)
                print("done")
                time.sleep(5)
                countdown = random.randint(5, 15)
                time.sleep(countdown)
                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()
                print("like done")
                time.sleep(2)

                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[3]/div[2]/div/div/div[1]/div[3]").click()
                time.sleep(2)
                print("done")
                time.sleep(5)
                countdown = random.randint(5, 15)
                time.sleep(countdown)
                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()
                print("like done")
                time.sleep(2)

                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[3]/div[2]/div/div/div[2]/div[2]/a/div").click()
                time.sleep(2)
                print("done")
                time.sleep(5)
                countdown = random.randint(5, 15)
                time.sleep(countdown)
                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()
                print("like done")
                time.sleep(2)
                countdown = random.randint(5, 15)
                time.sleep(countdown)
                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[3]/div[2]/div/div/div[2]/div[2]/a/div").click()
                time.sleep(2)
                print("done")
                time.sleep(5)
                countdown = random.randint(5, 15)
                time.sleep(countdown)
                driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()
                print("like done")
                time.sleep(2)

            except:
                # unfollow
                time.sleep(5)
                countdown = random.randint(0, 15)
                time.sleep(countdown)
                driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                # driver.get('https://www.instagram.com/')
                print("cancel user")
                time.sleep(3)
                countdown = random.randint(0, 15)
                time.sleep(countdown)
                # driver.close()
            else:
                time.sleep(3)
                print("garbage page")
                time.sleep(3)

    scroll()
    print("scroll done")
    time.sleep(5)
    countdown = random.randint(0, 15)
    time.sleep(countdown)
    like()
    print("like share done")
    return render(request, 'instgram.html')

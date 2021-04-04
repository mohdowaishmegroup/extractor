from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
import time
def indexun(request):
    return render(request,'unfollow.html')
def instaa(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('https://www.instagram.com/')
    time.sleep(5)
    print("done")
    def login():
        time.sleep(2)
        username=request.POST["users"]
        passw=request.POST["passs"]
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

    login()
    time.sleep(5)
    # profile show
    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span").click()
    # profile click
    time.sleep(5)

    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div").click()
    time.sleep(10)
    # followers
    time.sleep(5)
    # followers
    time.sleep(5)

    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
    print("done")
    scroll_box = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
    prev_height, height = 0, 1
    while prev_height != height:
        prev_height = height
        time.sleep(3)
        height = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight;
        """, scroll_box)
        time.sleep(5)
    print("ofn")
    links = scroll_box.find_elements_by_tag_name('a')
    followers = [name.text for name in links if name.text != '']
    close = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
    close.click()
    print(followers)
    total = len(followers) - 1
    print("total followers", total)
    # following
    # following
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
    following = []
    print("done")
    scroll_box = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
    prev_height, height = 0, 1
    while prev_height != height:
        prev_height = height
        time.sleep(3)
        height = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight;
        """, scroll_box)
        time.sleep(10)
    print("ofn")
    # get names
    links = scroll_box.find_elements_by_tag_name('a')
    following = [name.text for name in links if name.text != '']
    close = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
    close.click()
    print(following)
    total = len(following) - 1
    print("following total", total)

    # click on following button
    time.sleep(60)
    import random
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
    time.sleep(5)
    countdown = random.randint(0, 10)
    time.sleep(countdown)
    # Scroll the popup box
    print("done")
    scroll_box = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
    prev_height, height = 0, 1
    while prev_height != height:
        prev_height = height
        time.sleep(3)
        countdown = random.randint(0, 10)
        time.sleep(countdown)
        height = driver.execute_script("""
        arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight;
        """, scroll_box)
    print("ofn")

    # Iterate through all entities
    time.sleep(3)
    items = scroll_box.find_elements_by_tag_name('li')

    countdown = random.randint(0, 10)
    time.sleep(countdown)
    for item in items:
        a_elem = item.find_elements_by_tag_name('a')[0]
        btn_ref = item.find_elements_by_tag_name('button')[0]
        if (a_elem.text == ''):
            continue
            # print(a_elem.text)
            time.sleep(5)
            countdown = random.randint(0, 10)
            time.sleep(countdown)

        userName = a_elem.text
        if userName not in followers:
            btn_ref.click()
            time.sleep(10)
            countdown = random.randint(0, 30)
            time.sleep(countdown)
            unfollow = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
            unfollow.click()
            time.sleep(10)
            countdown = random.randint(0, 30)
            time.sleep(countdown)
            print("complete")
            print(userName)
            #print(unfollow)
            # print(items)
            context = {'username': userName,
                    }
            print("userName")
    return render(request, 'unfollow.html',context)

    # print(items)
from django.shortcuts import render, HttpResponse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
import pandas as pd
import time
import os
import csv
# User inp
def just(request):


    return render(request, 'just.html')
def testpath(request):

    return HttpResponse("this is services page");
    #return render(request, 'test.html')

def justdial(request):

    # User input Data
    search = request.POST["search"]
    locations = request.POST["locations"]

    #range = request.GET["range"]
    names = request.POST["names"]
    a = (search, locations)
    keyword = ' '.join(a)
    driver.get('https://www.justdial.com/')
    # Searching keyword

    searchbox = driver.find_element_by_xpath('/html/body/div[2]/section[1]/section[2]/section/div[2]/div/div[2]/input')
    searchbox.send_keys(keyword)

    # searchbox = driver.find_element_by_xpath('/html/body/div[2]/header/section/div/div[1]/div[2]/div/div[2]/div/div[2]/input')
    # searchbox.send_keys('Faridabad')

    searchButton = driver.find_element_by_xpath(
        '/html/body/div[2]/section[1]/section[2]/section/div[2]/div/span/button/span')
    searchButton.click()
    def script():
        import pandas as pd
        time.sleep(10)

        def strings_to_num(argument):

            switcher = {
                'dc': '+',
                'fe': '(',
                'hg': ')',
                'ba': '-',
                'acb': '0',
                'yz': '1',
                'wx': '2',
                'vu': '3',
                'ts': '4',
                'rq': '5',
                'po': '6',
                'nm': '7',
                'lk': '8',
                'ji': '9'
            }

            return switcher.get(argument, "nothing")

        storeDetails = driver.find_elements_by_class_name('store-details')

        nameList = []
        addressList = []
        numbersList = []

        for i in range(len(storeDetails)):

            name = storeDetails[i].find_element_by_class_name('lng_cont_name').text
            address = storeDetails[i].find_element_by_class_name('cont_fl_addr').get_attribute('innerHTML')
            contactList = storeDetails[i].find_elements_by_class_name('mobilesv')

            myList = []

            for j in range(len(contactList)):
                myString = contactList[j].get_attribute('class').split("-")[1]

                myList.append(strings_to_num(myString))

            nameList.append(name)
            addressList.append(address)
            numbersList.append("".join(myList))

        # intialise data of lists.
        data = {'Company Name': nameList,
                'Address': addressList,
                'Phone': numbersList}

        # Create DataFrame
        print("Script called")
        return data

    # search
    url = driver.current_url
    cookies = driver.get_cookies()
    driver.delete_all_cookies()
    driver.get(url)
    driver.delete_all_cookies()
    driver.execute_script("window.scrollTo(0,1500)")
    driver.get(url)
    driver.delete_all_cookies()
    driver.execute_script("window.scrollTo(1502,3500)")
    driver.get(url)
    driver.delete_all_cookies()
    driver.current_url
    time.sleep(7)
    data1 = script()
    # move to 2 page
    time.sleep(5)
    driver.current_url
    driver.get(url + '/page-2')
    driver.execute_script("window.scrollTo(0,3500)")
    driver.current_url
    time.sleep(5)
    data2 = script()

    # move to 3 page

   # data3 = script()

    # Creating data base

    df1 = pd.DataFrame(data1)
    time.sleep(1)
    df2 = pd.DataFrame(data2)
    time.sleep(1)
    #df3 = pd.DataFrame(data3)
    # creating page 3

    frame = [df1, df2]
    time.sleep(2)
    df = pd.concat(frame)

    header = ['S.no', 'Company Name', ' Address', 'Phone']
    df.to_csv("static\\datasets\\"f'{names}.csv', mode='w', header=True)
    context = {
        'filenames': f'{names}.csv',
        'locations': f'{locations}',
        'search': f'{search}',
    }

    print("Done")

    return render(request, 'just.html', context)

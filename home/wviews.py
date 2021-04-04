from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
import time
import re

def seo(request):

    return render(request, 'Seo Tools.html')

def web(request):
    # User input Data
    if "texta" in request.POST:
        locations = request.POST["texta"]
        file = request.POST["names"]
        url = str(locations)

        links = []
        name = []
        website = requests.get(url)
        text = website.text
        soup = BeautifulSoup(text)

        for link in soup.find_all('a'):
            links.append(link)

        # convert list to string
        textname = ' '.join(map(str, links))
        soup = BeautifulSoup(textname, 'lxml')
        tags = soup.find_all('a')
        name = []
        for i in tags:
            name.append(i.text)
        # convert list to string
        text = ' '.join(map(str, name))
        texts = text.lower()
        # texts = text.islower()
        names = texts.split()
        # create dict
        d = {}
        for word in names:
            d[word] = d.get(word, 0) + 1
        # create list
        words = []
        for key, value in d.items():
            words.append((value, key))
            words.sort(reverse=True)
        worde=words
        print("done")
        time.sleep(1)
        url = url
        links = []

        website = requests.get(url)
        text = website.text
        soup = BeautifulSoup(text)
        for link in soup.find_all('p'):
            links.append(link)
        text = ' '.join(map(str, links))
        # text = ' '.join(map(str, name))
        text = text.lower()
        for char in '<p></p>.,\n':
            text = text.replace(char, '')
        word_list = text.split()
        v = {}
        for word in word_list:
            v[word] = v.get(word, 0) + 1
        print("Done")
        # Python program to combine two dictionary
        # adding values for common keys
        # initializing two dictionaries
        dict1 = v
        dict2 = d

        # adding the values with common key
        for key in dict2:
            if key in dict1:
                dict2[key] = dict2[key] + dict1[key]
            else:
                pass

        c = dict2
        # print(dict2)
        # Python code to merge dict using update() method
        time.sleep(1)

        def Merge(dict1, dict2):
            return (dict2.update(dict1))

        # Driver code
        dict1 = c
        dict2 = v

        # This return None
        print(Merge(dict1, dict2))

        # changes made in dict2
        c = dict2
        word = []
        for key, value in c.items():
            word.append((value, key))
            word.sort(reverse=True)
        # list of strings
        lst = word
        # Calling DataFrame constructor on list
        df = pd.DataFrame(lst)
        time.sleep(1)
        df.to_csv("static\\datasets\\"f'{file}.csv', mode='w')
        context = {
            'filenames': f'{file}.csv',
            'locations': f'{url}',
            'commonkeyword': worde,
            'keyword': lst,
        }

        return render(request,'webc.html', context)
    else:
        return render(request, 'webc.html')

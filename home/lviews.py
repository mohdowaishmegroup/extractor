from django.shortcuts import render, HttpResponse
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
import time
def seo(request):


    return render(request, 'Seo Tools.html')


def link(request):
    from urllib.parse import urlparse

    # User input Data
    if "textc" in request.POST:
        locations = request.POST["textc"]
        names = request.POST["names"]
        url = str(locations)
        domain = urlparse(url).netloc
        print("domain",domain)

        links = []
        externalLinks = []
        internalLinks = []

        website = requests.get(url)
        text = website.text
        soup = BeautifulSoup(text)
        for link in soup.find_all('a'):
            links.append(link.get('href'))

        for link in links:

            domain1 = (urlparse(link).netloc)

            if domain1 == domain:

                internalLinks.append(link)

            else:
                externalLinks.append(link)
        a = set(externalLinks)
        a1 = set(internalLinks)
        b1 = list(a1)
        b = list(a)

        df = pd.DataFrame(b1, columns=['Internal Links'])
        df2 = pd.DataFrame(b, columns=['External Links'])
        frames = [df, df2]
        result = pd.concat(frames)

        tin = len(b1)
        tex = len(b)

        result.to_csv("static\\datasets\\"f'{names}.csv', mode='w')
        total = len(set(links))


        context = {
            'filenames': f'{names}.csv',
            'locations': f'{url}',
            'extLinks': a,
            'intLinks': a1,
            'totallinks': total,
            'totalint': tin,
            'totalexter': tex,

        }


        return render(request, 'links.html', context)
    else:
        return render(request, 'links.html')
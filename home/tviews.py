from django.shortcuts import render, HttpResponse
import re

def seo(request):

    return render(request, 'Seo Tools.html')

def wordCounter(request):

    # User input Data
    if "textc" in request.POST:
        text = request.POST["textc"]

        for char in '-.,\n':
            text = text.replace(char, '')
        text = text.lower()
        word_list = text.split()
        # initializing Dicitonary
        d = {}
        for word in word_list:
            d[word] = d.get(word, 0) + 1
            # if word not in d:
            #  d[word]=0
        # [word]+=1
        b=len(text)
        c=len(word_list)
        word = []
        for key, value in d.items():
            word.append((value, key))
        word.sort(reverse=True)
        listToStr = ' '.join(map(str, word))
        document = listToStr
        a = (re.sub('[()]', '\n', document))
        context = {
            'a': f'{a}',
            'b': f'{b}',
            'c': f'{c}',
        }
        return render(request, 'word.html', context)
    else:
        return render(request, 'word.html')


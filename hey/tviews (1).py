from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
import time
def indext(request):
    return render(request,'twitter.html')
from django.shortcuts import render, redirect,HttpResponse
#import request
from django.contrib.auth import authenticate, login

import pyrebase
from firebase import firebase
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from getpass import getpass
def fhome(request):

    return render(request, 'firebase.html')


# User input Data
def fire(request):

    firebaseConfig = {
        "apiKey": "AIzaSyCU-h440DmkaDmqb0UEKCpZ8d1W4nzQAEU",
        "authDomain": "pythondbtest-27bd9.firebaseapp.com",
        "databaseURL": "https://pythondbtest-27bd9-default-rtdb.firebaseio.com",
        "projectId": "pythondbtest-27bd9",
        "storageBucket": "pythondbtest-27bd9.appspot.com",
        "messagingSenderId": "701887967894",
        "appId": "1:701887967894:web:32c2d6cac25ebbecef48b7",
        "measurementId": "G-NZJ4SRZ9BV"
     }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    print('login...')
    # email = input("PLease Enter the Your Email Address: \n")
    # password = getpass("please Your passowrd: \n")
    try:
        email = request.POST["textq"]
        password = request.POST["passa"]
        login = auth.sign_in_with_email_and_password(email, password)
        print("succesfully loggin")
        auth.get_account_info(login['idToken'])
        a = auth.current_user['localId']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print("login")

        else:
            print("bye")

        # Return an 'invalid login' error message.

        context = {
            'filenames': login,

        }
        return render(request, 'result.html')

    except:

        print("invalid email password")
        return render(request, 'firebase.html')






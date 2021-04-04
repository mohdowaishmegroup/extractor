from django.shortcuts import render, HttpResponse
import csv
from googleplaces import GooglePlaces, types, lang

# Create your views here.
def index(request):
    #return HttpResponse("THis is homepage owaish");
    context={
        'variable1':'this is sent',
        'variable2':'owaish is always great'
    }

    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("this is about page");

def services(request):
    return HttpResponse("this is services page");

def add(request):

    API_KEY = 'AIzaSyDzF9-TvQl5vXA_MWFWiyBhX12p6n0Xj94'

    google_places = GooglePlaces(API_KEY)
    location = request.GET["location"]
    search = request.GET["search"]
    range = request.GET["range"]
    name = request.GET["name"]
    l = str(location)
    t = str(search)
    r = range * 1000
    r = int(r)
    query_result = google_places.nearby_search(
        location=l, keyword=search, radius=r)

    if query_result.has_attributions:
        print(query_result.html_attributions)

    # f=open('data.csv','a'
    with open("static\\datasets\\"f'{name}.csv', 'a', newline="") as writefile:
        csvwriter = csv.writer(writefile)
        csvwriter.writerow(["Name", "Address", "Rating", "Phone", "Location", "Website"])
        for place in query_result.places:
            place.get_details()
            csvwriter.writerow(
                [place.name, place.formatted_address, place.rating, place.international_phone_number, place.website])
        # print(place.name)
        writefile.close()

        context = {
            'filename': f'{name}.csv',
           # 'locationname': f'{location},
            'location': f'{location}',
            'search': f'{search}',
            'range': f'{range}',
        }

        return render(request, 'index.html', context)

from django.shortcuts import render
import json
import requests

def home(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=429224e9795ecb8ceda8068dd92a2fcb12az"
    
    if request.method == 'POST':

        city = request.POST.get('city')

        response = requests.get(url.format(city)).json()

        data = {
            'city': city,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
            'humidity': response['main']['humidity'],
        }

        context = {'data': data}
    
    else:
        data = {}
        context = {'data': data}

    return render(request, 'main/home.html', context)




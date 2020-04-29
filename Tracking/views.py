from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    response1 = requests.get('https://api.covid19api.com/summary')
    geodata1 = response1.json()
    return render(request, 'Tracking/dashboard.html', {
        'geodata': geodata1['Countries'],
        'global':geodata1['Global']
        
    })

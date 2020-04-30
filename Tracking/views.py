from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    response1 = requests.get('https://corona.lmao.ninja/v2/countries/bd')
    response2 = requests.get('https://corona.lmao.ninja/v2/all').json()

    geodata1 = response1.json()
    return render(request, 'Tracking/dashboard.html', {
        'geodata': geodata1,
        'global':response2
    })

'''def data(request):
	#curl --location --request GET 'https://api.covid19api.com/country/south-africa/status/confirmed'
	#url = "https://covid-19-data.p.rapidapi.com/report/country/all" #total

	#querystring = {"date-format":"YYYY-MM-DD","format":"json","date":"2020-04-25"}

	
	#url = "https://covid-19-data.p.rapidapi.com/country/code"

	#querystring = {"format":"json","code":"bd"}


	url = "https://covid-19-data.p.rapidapi.com/report/country/name"

	querystring = {"date-format":"YYYY-MM-DD","format":"json","date":"2020-04-30","name":"Bangladesh"}

	headers = {
	    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
	    'x-rapidapi-key': "152efa1ae8msh36c3ea07fcd4be0p17b15fjsn67fc5740c324"
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)

	return render(request,'Tracking/rapid.html', {'geodata': response.json()} )'''

'''def data (request):
	response = requests.get('https://api.covid19api.com/country/bangladesh/status/confirmed')
	geodata = response.json()

	return render(request,'Tracking/rapid.html', {'geodata': geodata} )'''
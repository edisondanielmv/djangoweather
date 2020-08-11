from django.shortcuts import render
def home (request):
	import json
	import requests


	if request.method == "POST":
		zipcode=request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=22DBDDD4-0237-4F58-8D1A-C7FE2ABE4BF2")

		try:
			api=json.loads(api_request.content)

		except Exception as e:
			api="Error..."


		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50) Good"
			category_color="good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51-100) Moderate"
			category_color="moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101-150) USG"
			category_color="usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200) Unhealthy"
			category_color="unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-250) Very unhealthy"
			category_color="veruunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(251-300) Hazardous"
			category_color="hazardous"


		#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=22DBDDD4-0237-4F58-8D1A-C7FE2ABE4BF2
		return render(request,'home.html',{
			'api':api, 
			'category_description':category_description, 
			'category_color':category_color
			})
			
	else:

		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=22DBDDD4-0237-4F58-8D1A-C7FE2ABE4BF2")

		try:
			api=json.loads(api_request.content)

		except Exception as e:
			api="Error..."


		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50) Good"
			category_color="good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51-100) Moderate"
			category_color="moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101-150) USG"
			category_color="usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200) Unhealthy"
			category_color="unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-250) Very unhealthy"
			category_color="veruunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(251-300) Hazardous"
			category_color="hazardous"


		#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=22DBDDD4-0237-4F58-8D1A-C7FE2ABE4BF2
		return render(request,'home.html',{
			'api':api, 
			'category_description':category_description, 
			'category_color':category_color
			})

def about (request):
	return render(request,'about.html',{})
# this is my views.py file

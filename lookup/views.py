from django.shortcuts import render
def home (request):
	return render(request,'home.html',{})

def about (request):
	return render(request,'about.html',{})
# this is my views.py file

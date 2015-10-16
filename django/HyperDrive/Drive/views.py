from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def login(request):
	return render(request,'profile.html')	

def profile(request):
    return render(request,'profile.html')

def logout(request):
	return render(request,'index.html')

def group(request):
	return render(request,'group.html')

def personal(request):
	return render(request,'personal.html')

def addplace(request):
	return render(request,'addplace.html')	
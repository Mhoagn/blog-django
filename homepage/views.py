from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'homepage/homepage.html')

def contact(request):
    return render(request,'homepage/contact.html')

def about(request):
    return render(request,'homepage/about.html')
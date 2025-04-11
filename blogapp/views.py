from django.shortcuts import render,HttpResponse

# Create your views here.

def bloghome(request):
    return HttpResponse("This is blog home page")

def blogpost(request,slug):
    return HttpResponse(f'This is blog post: {slug}')
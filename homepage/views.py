from django.shortcuts import render,HttpResponse,redirect
from .models import ContactUser
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'homepage/homepage.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name and email and phone and message:
            contact_user = ContactUser(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            contact_user.save()
            messages.success(request, "Gửi liên hệ thành công! Chúng tôi sẽ phản hồi bạn sớm nhất.")
            return redirect('contact') 
        else:
            messages.error(request, "Vui lòng điền đầy đủ thông tin!")

    return render(request, 'homepage/contact.html')

def about(request):
    return render(request,'homepage/about.html')
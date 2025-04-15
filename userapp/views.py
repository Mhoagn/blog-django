from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, UserLoginForm
from django.contrib import messages

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'user'  # mặc định là user
            user.save()
            messages.success(request, 'Đăng ký thành công!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        print("Form submitted")
        print(f"POST data: {request.POST}")  # In ra dữ liệu POST
        
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"Attempting login with username: {username}")
            
            user = authenticate(request, username=username, password=password)
            print(f"Authentication result: {user}")
            
            if user is not None:
                login(request, user)
                print("Login successful")
                return redirect('home')  # Đảm bảo 'home' là tên URL pattern của trang chủ
            else:
                print("Authentication failed")
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không chính xác!')
        else:
            print(f"Form errors: {form.errors}")
            messages.error(request, 'Vui lòng kiểm tra lại thông tin đăng nhập!')
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

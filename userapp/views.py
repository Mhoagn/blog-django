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
        print("Form submitted") # Debug
        if form.is_valid():
            print("Form is valid") # Debug
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(f"User authenticated: {user}") # Debug
            if user is not None:
                login(request, user)
                print("User logged in successfully") # Debug
                return redirect('home')  # Thay 'home' bằng tên URL pattern của homepage của bạn
            else:
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không chính xác!')
        else:
            print(f"Form errors: {form.errors}") # Debug
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

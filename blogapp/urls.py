from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),  # Trang chủ blog
    path('<str:slug>/', views.blogpost, name='blogpost'),  # Chi tiết bài viết
]

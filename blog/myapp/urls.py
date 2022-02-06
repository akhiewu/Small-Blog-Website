from django.urls import path
from . import views


urlpatterns = [
    path('', views.deshboard, name='Dashboard'),
    path('home/', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact')
    
]

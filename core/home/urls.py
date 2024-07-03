from django.urls import path
from home import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('about',views.about, name='about'),
    path('services',views.education, name='education'),
    path('skills',views.skills, name='skills'),
    path('teams',views.experience, name='experience'),
    path('contact',views.contact, name='contact'),
]

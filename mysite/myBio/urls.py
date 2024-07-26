from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name= 'about'),
    path('resume/', views.resume, name='resume'),
    path("contact/", views.contact_view, name="contact")
]

from django.urls import path
from . import views
from .views import contact_view
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name= 'about'),
    path('resume/', views.resume, name='resume'),
    path("contact/", views.contact_view, name="contact"),
    path('success/', views.contact_success_view, name='success'),
]

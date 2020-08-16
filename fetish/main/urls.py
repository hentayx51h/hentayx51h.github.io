from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('pricing', views.pricing, name='pricing'),
    path('sign-in', views.signin, name='signin'),
]

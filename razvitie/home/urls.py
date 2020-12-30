from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send_email, name='email'),
    path('review/', views.add_review, name='review'),
]

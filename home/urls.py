from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.base,name="base"),
    path('loogin',views.loogin,name="loogin"),
    path('qurey_form',views.qurey_form,name="qurey_form"),
    path('sign_up', views.sign_up,name="sign_up"),
    path('blogs', views.blogs,name="blogs"),
    path('info', views.info,name="info"),
    path('loogout',views.loogout,name="loogout")
]

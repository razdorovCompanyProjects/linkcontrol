from django.urls import path, include
from .views import index,search

urlpatterns = [
    path('control/<str:id>/', index),
    path('', search),

]

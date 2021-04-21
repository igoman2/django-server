from django.urls import path,include
from .views import helloAPI
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path("hello/", helloAPI)
]
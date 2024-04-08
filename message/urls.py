from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('message', messages, name="message"),
    path('nasılCalisir', nasılÇalışır, name="nasılÇalışır")
]
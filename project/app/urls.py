from django.urls import path
from app.views import *

urlpatterns = [
    path("", Login.as_view(),name='login'),
    path("otp/", Otpverification.as_view(),name='otp'),
]

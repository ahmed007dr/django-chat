from django.urls import path

from . import views
from .views import frontpage ,singup


urlpatterns = [
    path('',frontpage),
    path('singup/',singup),
]


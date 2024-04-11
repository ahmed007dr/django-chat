from django.urls import path

from . import views
from .views import frontpage


urlpatterns = [
    path('',frontpage),
]


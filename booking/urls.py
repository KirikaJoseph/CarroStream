from django.urls import path
from . import views

urlpatterns = [
    # Define your routes here, e.g.,
path('booking', views.booking, name='booking'),
]
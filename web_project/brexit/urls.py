from django.urls import path
from brexit import views

urlpatterns = [
    path("", views.home, name="home"),
    
]
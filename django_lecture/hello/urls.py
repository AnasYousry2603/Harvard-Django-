from django.urls import path
from . import views
# list of the allowable urls that can be accessed
urlpatterns = [
    path("", views.index, name="index"),
    path("Anas", views.Anas, name="Anas"), 
    path("<str:name>", views.greet, name="greet")
]
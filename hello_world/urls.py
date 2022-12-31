from django.urls import path
from . import views

urlpatterns = [
    # Urls go here
    path("", views.hello_world, name="hello_world"),
]
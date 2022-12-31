from django.urls import path
from . import views

urlpatterns = [
    # Urls go in here
    path("", views.index, name="index"),
    path('<int:pk>/', views.detail, name="detail"),
    path("<category>/", views.category, name="category"),
]
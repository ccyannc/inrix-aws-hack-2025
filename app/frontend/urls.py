from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("", views.index, name="index"),
    path("upload/", views.upload_file_view, name="upload"),
    path("results/", views.results_view, name="results"),
    path('index/', views.index, name='index'),
]
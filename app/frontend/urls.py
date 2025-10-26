from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.upload_file_view, name="upload_file"),
    path("results/", views.results_view, name="results"),
]
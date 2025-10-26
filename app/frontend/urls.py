from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file_view, name='home'),          # 👈 This handles http://127.0.0.1:8000/
    path('upload/', views.upload_file_view, name='upload_file'),
]
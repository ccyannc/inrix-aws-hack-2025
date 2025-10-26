from django.db import models
from django.contrib.auth.models import User

class UserSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="systems")
    xray_image_url = models.URLField() 
    diagnosis = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s upload at {self.uploaded_at}"

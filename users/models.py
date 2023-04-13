from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user.username}'
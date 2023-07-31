from django.db import models
from django.contrib.auth.models import User
import uuid
# from django.utils import timezone



# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,   on_delete=models.CASCADE,related_name="profile")
    phone_number=models.CharField(max_length=15)
    otp=models.CharField(max_length=100, null=True, blank=True)
    uid=models.CharField(default=uuid.uuid4, max_length=200)

    
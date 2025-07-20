from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from ecom_prj.models import BaseModel

USER_TYPE = (
    ("Vendor", "Vendor"),
    ("Customer", "Customer"),
)

# Create your models here.
class User(AbstractUser, BaseModel):
    # Custom user model that extends the default Django user model.
    # Add any additional fields you want here

    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    

    def save(self, *args, **kwargs):
        email_username, _ = self.email.split('@')
        if not self.username:
            self.username = email_username
        super(User, self).save(*args, **kwargs)



class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to="profile_images/", default='default.jpg', null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.CharField(max_length=255, choices=USER_TYPE, null=True, blank=True)
    

    def __str__(self):
        return self.user.username
    

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = self.user.get_full_name()
        super(Profile, self).save(*args, **kwargs)
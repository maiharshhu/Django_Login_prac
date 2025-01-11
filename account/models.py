from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model with is_admin and is_user flags
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)

    def __str__(self):
        return self.username

# App data model for storing information about the apps
class appdata(models.Model):
    app_name = models.CharField(max_length=100)
    app_link = models.URLField()
    app_points = models.PositiveIntegerField()

    def __str__(self):
        return self.app_name

# User data model for storing user points and screenshots
class user_data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User
    app = models.ForeignKey(appdata, on_delete=models.CASCADE)  # Correct field name for app relationship
    points = models.PositiveIntegerField()  # Store points for the app
    screenshot = models.ImageField(upload_to='media/images/')  # Store screenshot uploaded by user

    def __str__(self):
        return f'{self.user.username} - {self.app.app_name}'  # Corrected string representation

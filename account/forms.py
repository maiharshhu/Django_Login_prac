from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, appdata, user_data

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

# Sign Up Form (for both admins and regular users)
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    # Only allow 'is_user' for normal users
    is_user = forms.BooleanField(
        required=False,
        initial=True,  # Default is 'True' (since regular users will be 'is_user')
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    # We don't show 'is_admin' to regular users (handled in the view)
    is_admin = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_user')


# App Data Form (for admins to add new apps)
class AppDataForm(forms.ModelForm):
    class Meta:
        model = appdata
        fields = ('app_name', 'app_link', 'app_points')
        widgets = {
            'app_name': forms.TextInput(attrs={'class': 'form-control'}),
            'app_link': forms.URLInput(attrs={'class': 'form-control'}),
            'app_points': forms.NumberInput(attrs={'class': 'form-control'})
        }

# User Data Form (for admins to assign points to users)
class UserDataForm(forms.ModelForm):
    class Meta:
        model = user_data
        fields = ('user', 'app', 'points', 'screenshot')  # Ensure these fields exist in the model
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for selecting a user
            'app': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for selecting an app
            'points': forms.NumberInput(attrs={'class': 'form-control'}),  # Input for points
            'screenshot': forms.ClearableFileInput(attrs={'class': 'form-control'})  # File input for screenshots
        }

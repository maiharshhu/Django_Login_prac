from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from .forms import SignUpForm, LoginForm, AppDataForm, UserDataForm
from .models import appdata, user_data

# Custom decorator for admin access
def admin_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.is_admin)(view_func)

# Function to determine the redirect URL based on user role
def get_redirect_url(user):
    if user.is_admin:
        return reverse('admin_page')
    elif user.is_user:
        return reverse('user_page')
    return reverse('login_view')

# Admin dashboard view
@admin_required
def admin_dashboard(request):
    apps = appdata.objects.all()  
    users = user_data.objects.all()  

    # Initialize forms with prefixes
    if request.method == 'POST':
        app_form = AppDataForm(request.POST, prefix='app')
        user_form = UserDataForm(request.POST, request.FILES, prefix='user')

        if app_form.is_valid():
            app_form.save()  # Save app data
            return redirect('admin_page')
        elif user_form.is_valid():
            user_form.save()  # Save user data
            return redirect('admin_page')
    else:
        app_form = AppDataForm(prefix='app')  # Empty app form
        user_form = UserDataForm(prefix='user')  # Empty user form

    return render(request, 'admin.html', {
        'apps': apps,
        'users': users,
        'app_form': app_form,
        'user_form': user_form
    })

# Index page
def index(request):
    return render(request, 'index.html')

# User registration view
def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Handle admin role if the user is an admin
            if request.user.is_authenticated and request.user.is_admin:
                is_admin = form.cleaned_data.get('is_admin', False)
                user.is_admin = is_admin

            user.is_user = form.cleaned_data.get('is_user', True)  # Default is_user = True
            user.save()
            return redirect('login_view')
        else:
            msg = 'Please correct the errors below.'

    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form, 'msg': msg, 'errors': form.errors if form.errors else None})

# Login view
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(get_redirect_url(user))
        else:
            msg = 'Invalid credentials'

    return render(request, 'login.html', {'form': form, 'msg': msg})

# User page view
def user_page(request):
    return render(request, 'user_page.html')

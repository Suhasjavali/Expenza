from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView, LogoutView
from expenses.models import Category

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = 'login'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            messages.success(request, 'You have been logged out successfully.')
            return super().dispatch(request, *args, **kwargs)
        return self.get(request, *args, **kwargs)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create default categories for the new user
            default_categories = [
                'Food & Dining',
                'Transportation',
                'Shopping',
                'Entertainment',
                'Bills & Utilities',
                'Health & Fitness',
                'Travel',
                'Education',
                'Gifts & Donations',
                'Other'
            ]
            
            for category_name in default_categories:
                Category.objects.create(
                    name=category_name,
                    user=user,
                    description=f"Default {category_name} category"
                )
            
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})

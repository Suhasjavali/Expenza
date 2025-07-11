from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove password validation messages
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        # Make email optional
        self.fields['email'].required = False

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'address', 'profile_picture')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'address', 'profile_picture')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        } 
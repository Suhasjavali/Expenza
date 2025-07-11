from django import forms
from .models import Expense, Category, Budget
from django.core.exceptions import ValidationError
from datetime import date

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description', 'date', 'payment_method', 'receipt']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Create default categories if they don't exist
            default_categories = [
                ('Food & Dining', 'Expenses related to food and dining out'),
                ('Transportation', 'Transportation related expenses'),
                ('Shopping', 'Shopping and retail expenses'),
                ('Entertainment', 'Entertainment and leisure expenses'),
                ('Bills & Utilities', 'Monthly bills and utilities'),
                ('Health & Fitness', 'Health and fitness related expenses'),
                ('Travel', 'Travel and vacation expenses'),
                ('Education', 'Education and learning expenses'),
                ('Gifts & Donations', 'Gifts and charitable donations'),
                ('Other', 'Miscellaneous expenses')
            ]
            
            for name, description in default_categories:
                Category.objects.get_or_create(
                    name=name,
                    user=user,
                    defaults={'description': description}
                )
            
            # Get all user's categories
            self.fields['category'].queryset = Category.objects.filter(user=user).order_by('name')
            
            # Set the first category as default
            if self.fields['category'].queryset.exists():
                self.fields['category'].initial = self.fields['category'].queryset.first()

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'amount', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            # Create default categories if they don't exist
            default_categories = [
                ('Food & Dining', 'Expenses related to food and dining out'),
                ('Transportation', 'Transportation related expenses'),
                ('Shopping', 'Shopping and retail expenses'),
                ('Entertainment', 'Entertainment and leisure expenses'),
                ('Bills & Utilities', 'Monthly bills and utilities'),
                ('Health & Fitness', 'Health and fitness related expenses'),
                ('Travel', 'Travel and vacation expenses'),
                ('Education', 'Education and learning expenses'),
                ('Gifts & Donations', 'Gifts and charitable donations'),
                ('Other', 'Miscellaneous expenses')
            ]
            
            for name, description in default_categories:
                Category.objects.get_or_create(
                    name=name,
                    user=user,
                    defaults={'description': description}
                )
            
            # Get all user's categories
            self.fields['category'].queryset = Category.objects.filter(user=user).order_by('name')
            
            # Set the first category as default
            if self.fields['category'].queryset.exists():
                self.fields['category'].initial = self.fields['category'].queryset.first()

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        amount = cleaned_data.get('amount')

        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError("Start date cannot be after end date.")
            if start_date < date.today():
                raise ValidationError("Start date cannot be in the past.")

        if amount is not None and amount <= 0:
            raise ValidationError("Amount must be greater than zero.")

        return cleaned_data 
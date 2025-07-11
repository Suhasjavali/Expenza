from django.contrib import admin
from .models import Category, Expense, Budget

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'date', 'payment_method', 'created_at')
    list_filter = ('user', 'category', 'payment_method', 'date')
    search_fields = ('description', 'category__name')
    ordering = ('-date',)
    date_hierarchy = 'date'

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'start_date', 'end_date', 'created_at')
    list_filter = ('user', 'category', 'start_date', 'end_date')
    search_fields = ('category__name',)
    ordering = ('-created_at',)
    date_hierarchy = 'start_date'

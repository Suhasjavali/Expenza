from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/create/', views.expense_create, name='expense_create'),
    path('expenses/<int:pk>/update/', views.expense_update, name='expense_update'),
    path('expenses/<int:pk>/delete/', views.expense_delete, name='expense_delete'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('budgets/', views.budget_list, name='budget_list'),
    path('budgets/create/', views.budget_create, name='budget_create'),
    path('budgets/<int:pk>/update/', views.budget_update, name='budget_update'),
    path('budgets/<int:pk>/delete/', views.budget_delete, name='budget_delete'),
] 
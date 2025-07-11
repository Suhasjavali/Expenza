from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta
from .models import Expense, Category, Budget
from .forms import ExpenseForm, CategoryForm, BudgetForm

@login_required
def dashboard(request):
    # Get current month's expenses
    current_month = timezone.now().month
    current_year = timezone.now().year
    
    monthly_expenses = Expense.objects.filter(
        user=request.user,
        date__month=current_month,
        date__year=current_year
    )
    
    # Calculate total expenses for current month
    total_expenses = monthly_expenses.aggregate(total=Sum('amount'))['total'] or 0
    
    # Get expenses by category
    expenses_by_category = monthly_expenses.values('category__name').annotate(
        total=Sum('amount')
    ).order_by('-total')
    
    # Get recent expenses
    recent_expenses = monthly_expenses.order_by('-date')[:5]
    
    # Get budgets
    budgets = Budget.objects.filter(
        user=request.user,
        start_date__lte=timezone.now().date(),
        end_date__gte=timezone.now().date()
    )
    
    context = {
        'total_expenses': total_expenses,
        'expenses_by_category': expenses_by_category,
        'recent_expenses': recent_expenses,
        'budgets': budgets,
    }
    
    return render(request, 'expenses/dashboard.html', context)

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

@login_required
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm(user=request.user)
    return render(request, 'expenses/expense_form.html', {'form': form})

@login_required
def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense, user=request.user)
    return render(request, 'expenses/expense_form.html', {'form': form})

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'expenses/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Category added successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'expenses/category_form.html', {'form': form})

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'expenses/budget_list.html', {'budgets': budgets})

@login_required
def budget_create(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST, user=request.user)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request, 'Budget added successfully!')
            return redirect('budget_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.title()}: {error}")
    else:
        form = BudgetForm(user=request.user)
        # Set default dates
        today = timezone.now().date()
        form.initial = {
            'start_date': today,
            'end_date': today + timedelta(days=30)
        }
    return render(request, 'expenses/budget_form.html', {'form': form})

@login_required
def budget_update(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Budget updated successfully!')
            return redirect('budget_list')
    else:
        form = BudgetForm(instance=budget, user=request.user)
    return render(request, 'expenses/budget_form.html', {'form': form})

@login_required
def budget_delete(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    if request.method == 'POST':
        budget.delete()
        messages.success(request, 'Budget deleted successfully!')
        return redirect('budget_list')
    return render(request, 'expenses/budget_confirm_delete.html', {'budget': budget})

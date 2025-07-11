# Expenza

Expenza is a modern, user-friendly expense tracker web application built with Django. It helps users manage their personal finances, track expenses, set budgets, and visualize spending patterns.

## Features
- User registration, login, and profile management
- Add, edit, and delete expenses, categories, and budgets
- Dashboard with charts and recent expenses
- Upload and view receipt images
- Responsive UI with Bootstrap and Chart.js
- Django Admin for backend management

## Tech Stack
- Python, Django
- SQLite (default, can be changed)
- HTML, CSS, JavaScript, Bootstrap, Chart.js

## Getting Started
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`
5. Access at `http://127.0.0.1:8000/`

## Folder Structure
- `expense_tracker/` – Django project settings
- `expenses/` – Main app for expense management
- `users/` – User authentication and profiles
- `templates/` – HTML templates
- `static/` – Static files (CSS, JS)
- `media/` – Uploaded receipts

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from expenses.models import Category

User = get_user_model()

class Command(BaseCommand):
    help = 'Adds default categories for all users'

    def handle(self, *args, **options):
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

        users = User.objects.all()
        for user in users:
            for name, description in default_categories:
                Category.objects.get_or_create(
                    name=name,
                    user=user,
                    defaults={'description': description}
                )
            self.stdout.write(self.style.SUCCESS(f'Added default categories for user {user.username}')) 
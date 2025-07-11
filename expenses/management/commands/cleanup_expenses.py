from django.core.management.base import BaseCommand
from django.utils import timezone
from expenses.models import Expense
from datetime import timedelta

class Command(BaseCommand):
    help = 'Clean up old expenses'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=365,
            help='Number of days to keep expenses (default: 365)'
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be deleted without actually deleting'
        )

    def handle(self, *args, **options):
        days = options['days']
        dry_run = options['dry_run']
        
        # Calculate cutoff date
        cutoff_date = timezone.now() - timedelta(days=days)
        
        # Get expenses to delete
        expenses = Expense.objects.filter(date__lt=cutoff_date)
        
        if dry_run:
            self.stdout.write(
                self.style.WARNING(
                    f'DRY RUN: Would delete {expenses.count()} expenses older than {cutoff_date.date()}'
                )
            )
            return
        
        # Delete expenses
        count = expenses.count()
        expenses.delete()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully deleted {count} expenses older than {cutoff_date.date()}'
            )
        ) 
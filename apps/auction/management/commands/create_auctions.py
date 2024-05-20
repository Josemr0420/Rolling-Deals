# your_app_name/management/commands/create_auctions.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from apps.auction.models import Hotwheel, Auction

User = get_user_model()

class Command(BaseCommand):
    help = 'Create auctions for all Hot Wheels'

    def handle(self, *args, **kwargs):
        auction_duration = timedelta(days=7)  # Example: 7 days auction duration
        starting_bid = 10.00  # Example: starting bid
        default_user = User.objects.first()  # Assuming the first user is the default user

        if not default_user:
            self.stdout.write(self.style.ERROR('No users found in the database.'))
            return

        hotwheels = Hotwheel.objects.all()

        if not hotwheels.exists():
            self.stdout.write(self.style.ERROR('No Hot Wheels found in the database.'))
            return

        for hotwheel in hotwheels:
            start_time = timezone.now()
            end_time = start_time + auction_duration
            Auction.objects.create(
                hotwheel=hotwheel,
                start_time=start_time,
                end_time=end_time,
                status='upcoming',
                starting_bid=starting_bid,
                user=default_user
            )

        self.stdout.write(self.style.SUCCESS('Auctions created successfully!'))

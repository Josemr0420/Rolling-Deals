from django.conf import settings
from django.db import models
from django.utils import timezone


class Hotwheel(models.Model):
    model_name = models.CharField(max_length=255)
    year_released = models.IntegerField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='hotwheels/', blank=True, null=True)

    def __str__(self):
        return self.model_name


class Auction(models.Model):
    STATUS_CHOICES = (
        ('active', 'Activa'),
        ('completed', 'Terminada'),
        ('upcoming', 'Por hacer'),
    )

    hotwheel = models.ForeignKey(Hotwheel, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='auctions')

    def __str__(self):
        return f"{self.hotwheel.model_name} - {self.status}"


class Bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bids')
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.auction.hotwheel.model_name}"

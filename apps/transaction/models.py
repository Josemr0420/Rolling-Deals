from django.db import models
from django.conf import settings

# Create your models here.
class Transaction(models.Model):
    TransactionID = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    date = models.DateField()
    details = models.CharField(max_length=500)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.TransactionID


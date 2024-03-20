from django.db import models
from django.conf import settings

# Create your models here.
class Rating(models.Model):
    ratingID = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    score_choices = [
        ('1',1),('2',2),('3',3),('4',4),('5',5)
    ]
    score = models.CharField(max_length=1,choices=score_choices)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return f"Rating ID: {self.ratingID}, Score: {self.score}, User: {self.user}"
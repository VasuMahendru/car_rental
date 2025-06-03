
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.model})"
    
class Feedback(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='feedbacks')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('car', 'user')
    def __str__(self):
        return f'Feedback by {self.user.username} for {self.car.make} {self.car.model}'

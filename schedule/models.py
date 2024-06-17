from django.db import models
from services.models import Services


# Create your models here.
class Schedule(models.Model):
    HOUR_CHOICE = [('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'),
                   ('13:00','13:00'), ('14:00','14:00'), ('15:00', '15:00'), 
                   ('16:00','16:00'), ('17:00','17:00'), ('18:00','18:00'), ('19:00','19:00')]
    
    customer_name = models.CharField(max_length=100)
    day_schedule = models.DateTimeField()
    time_schedule = models.CharField(max_length=10, choices=HOUR_CHOICE)
    services = models.ManyToManyField(Services)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    class Meta:
        ordering = ['day_schedule']
    

    def __str__(self):
        return self.customer_name

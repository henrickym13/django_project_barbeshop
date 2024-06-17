from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)
      

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    num_guests = models.PositiveIntegerField()
    reservation_time = models.DateTimeField()


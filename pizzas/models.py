from django.db import models

PIZZA_TYPES = (
    ('REGULAR', 'Regular'),
    ('SQUARE', 'Square'),
)

class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=PIZZA_TYPES)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
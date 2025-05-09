from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    quantity= models.IntegerField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
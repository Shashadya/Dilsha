from django.db import models

# Create your models here.
# All of our Products

# Define Category model or import it if defined elsewhere


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # @daverobb2011


class Meta:
    verbose_name_plural = 'categories'


# All of our Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    more_info = models.TextField(
        max_length=1000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')

    # Add Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name

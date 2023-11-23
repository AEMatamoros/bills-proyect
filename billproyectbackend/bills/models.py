from django.db import models

# Create your models here.
class Product(models.Model):
    CHOICES = (
        ('J', 'Jardineria'),
        ('L', 'Limpieza'),
        ('A', 'Autos'),
        ('H', 'Hogar'),
        ('C', 'Comida'),
        ('O', 'Otros'),
    )
    name = models.CharField(verbose_name = 'Name', max_length = 50)
    description = models.CharField(verbose_name = 'Description', max_length = 100 )
    price = models.FloatField(verbose_name = 'Precio')
    discount = models.IntegerField(verbose_name = 'Descuento')
    category = models.CharField(verbose_name='Categoria',choices = CHOICES, default='O', max_length = 5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}  {self.name}'

class Bill(models.Model):
    products = models.ManyToManyField(Product)
    subtotal = models.FloatField(verbose_name = 'Subtotal')
    total = models.FloatField(verbose_name = 'Subtotal')
    client_name = models.CharField(verbose_name = 'ClientName', max_length = 50)
    rtn = models.IntegerField(verbose_name = 'RTN')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

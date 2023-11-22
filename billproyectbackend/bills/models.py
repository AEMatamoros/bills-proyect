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
    price = models.IntegerField(verbose_name = 'Precio')
    category = models.CharField(verbose_name='Categoria',choices = CHOICES, default='O', max_length = 5)

    def __str__(self):
        return f'{self.id}  {self.name}'
    

    
from django.db import models

# Create your models here.


class Product(models.Model):
    CHOICES = (
        ('J', 'Jardineria'),
        ('L', 'Limpieza'),
        ('A', 'Autos'),
        ('H', 'Hogar'),
        ('C', 'Comida'),
        ('T', 'Tecnologia'),
        ('O', 'Otros'),
    )
    name = models.CharField(verbose_name='Nombre', max_length=50)
    description = models.CharField(verbose_name='Descripcion', max_length=100)
    price = models.FloatField(verbose_name='Precio')
    discount = models.IntegerField(
        verbose_name='Descuento', null=True, blank=True)
    category = models.CharField(
        verbose_name='Categoria', choices=CHOICES, default='O', max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="uploads/",
                              null=True, blank=True, verbose_name='Imagen')

    def __str__(self):
        return f'{self.id}  {self.name}'


class SellDetail(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product", verbose_name="Producto")
    quantity = models.IntegerField(verbose_name="Cantidad")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creacion")

    def __str__(self):
        return f'{self.product.name}  {self.quantity}'


class Bill(models.Model):
    selldetail = models.ManyToManyField(
        SellDetail, related_name="selldetail", blank=True, verbose_name="Detalles de la venta")
    client_name = models.CharField(
        verbose_name='Nombre del Cliente', max_length=50)
    rtn = models.IntegerField(verbose_name='RTN', blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha Creacion")
    subtotal = models.FloatField(
        verbose_name='Subtotal', blank=True, null=True)
    total = models.FloatField(verbose_name='Total', blank=True, null=True)

    def __str__(self):
        return f'{self.client_name}  {self.created_at}'

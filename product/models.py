from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categorias"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category,  null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.description

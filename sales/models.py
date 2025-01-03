from datetime import datetime
from django.db import models
from django.db.models import Sum, F, FloatField
from django.db.models.signals import post_save
from django.dispatch import receiver
from clients.models import Client
from product.models import Product
from django.utils.translation import gettext_lazy as _
from .managers import SaleManager

CREATED = 'Criado'
PAID = 'Pago'
SHIPPED = 'Enviado'
REFUNDED = 'Devolveu'

SALE_STATUS_CHOICES = (
    (CREATED, _('Criado')),
    (PAID, _('Pago')),
    (SHIPPED, _('Enviado')),
    (REFUNDED, _('Devolveu')),
)


class Sale(models.Model):
    class Meta:
        verbose_name_plural = "Vendas"
    tax = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True)
    client = models.ForeignKey(Client, null=False, blank=False, on_delete=models.PROTECT)
    datetime = models.DateTimeField(default=datetime.now, blank=False, null=False)
    status = models.CharField(max_length=120, default='created', choices=SALE_STATUS_CHOICES)
    total = models.DecimalField(default=0.00, null=False, blank=False, max_digits=100, decimal_places=2)

    objects = SaleManager()

    def calc_total(self):
        tot = self.item_set.all().aggregate(
            total_ord=Sum((F('quantity') * F('products__price')) - F('discount'), output_field=FloatField())
        )['total_ord'] or 0

        tot = tot - float(self.tax) - float(self.discount)
        self.total = tot
        Sale.objects.filter(id=self.id).update(total=tot)

    def __str__(self):
        return str(self.id)


class Item(models.Model):
    class Meta:
        verbose_name_plural = "Itens"
    products = models.ForeignKey(Product, null=False, blank=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True)
    sales = models.ForeignKey(Sale, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return self.products.name


@receiver(post_save, sender=Item)
def update_sales_total(sender, instance, **kwargs):
    instance.sales.calc_total()


@receiver(post_save, sender=Sale)
def update_sales_total2(sender, instance, **kwargs):
    instance.calc_total()

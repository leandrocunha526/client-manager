from django.db import models
from django.db.models import Max, Avg, Min, Count


class SaleManager(models.Manager):

    def media(self):
        return self.all().aggregate(Avg('total'))['total__avg']

    def media_discount(self):
        return self.all().aggregate(Avg('discount'))['discount__avg']

    def media_tax(self):
        return self.all().aggregate(Avg('tax'))['tax__avg']

    def min(self):
        return self.all().aggregate(Min('total'))['total__min']

    def max(self):
        return self.all().aggregate(Max('total'))['total__max']

    def number_sale(self):
        return self.all().aggregate(Count('id'))['id__count']

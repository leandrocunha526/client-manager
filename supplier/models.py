from django.db import models


class Supplier(models.Model):
    class Meta:
        verbose_name_plural = "Fornecedores"
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    street_address = models.CharField(max_length=255)
    number = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    district = models.CharField(max_length=80, blank=True, null=True)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

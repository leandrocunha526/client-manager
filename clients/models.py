from django.db import models


class Document(models.Model):
    class Meta:
        verbose_name_plural = "Documentos"
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    class Meta:
        verbose_name_plural = "Pessoas"
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    biography = models.TextField()
    photo = models.ImageField(upload_to='client_photos', null=True, blank=True)
    document = models.OneToOneField(Document, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Product(models.Model):
    class Meta:
        verbose_name_plural = "Produtos"
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.description


class Sale(models.Model):
    class Meta:
        verbose_name_plural = "Vendas"
    number = models.CharField(max_length=7)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    taxes = models.DecimalField(max_digits=5, decimal_places=2)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.number

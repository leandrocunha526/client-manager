from django.db import models


class Client(models.Model):
    class Meta:
        verbose_name_plural = "Clientes"
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    biography = models.TextField()
    photo = models.ImageField(upload_to='client_photos', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

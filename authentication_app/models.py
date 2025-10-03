from django.db import models

# Modelo Country (tabla de países)
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre del país")
    abbrev = models.CharField(max_length=10, unique=True, verbose_name="Abreviatura")
    status = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.abbrev})"

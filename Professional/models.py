from django.db import models


class Professional(models.Model):
    name = models.CharField(max_length=255)  # Nome completo
    phone = models.CharField(max_length=20)  # Telefone
    email = models.EmailField(unique=True)  # E-mail único
    cpf = models.CharField(max_length=14, unique=True)  # CPF único
    crp = models.CharField(max_length=20, unique=True)  # Número do CRP
    bio = models.TextField(blank=True, null=True)  # Biografia
    specialties = models.CharField(max_length=255)  # Especialidades

    def __str__(self):
        return self.name
# Create your models here.

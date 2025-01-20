from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)  # Nome real
    email = models.EmailField(unique=True)  # E-mail único
    password = models.CharField(max_length=255)  # Senha (armazenada com hash)
    nickname = models.CharField(max_length=255, unique=True)  # Codinome para anonimato

    def __str__(self):
        return self.nickname
# Create your models here.

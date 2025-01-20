# Generated by Django 5.1.5 on 2025-01-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('crp', models.CharField(max_length=20, unique=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('specialties', models.CharField(max_length=255)),
            ],
        ),
    ]

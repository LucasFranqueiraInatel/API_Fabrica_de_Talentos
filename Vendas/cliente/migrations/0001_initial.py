# Generated by Django 3.1.1 on 2023-01-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('cep', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(max_length=40)),
                ('senha', models.CharField(max_length=20)),
                ('telefone', models.CharField(blank=True, max_length=14, null=True)),
            ],
        ),
    ]

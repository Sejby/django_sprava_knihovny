# Generated by Django 5.0.2 on 2024-03-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zaznam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev_knihy', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('zanr', models.CharField(max_length=50)),
                ('pocet_stran', models.IntegerField()),
                ('datum_vytvoreni', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
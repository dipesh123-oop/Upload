# Generated by Django 3.0.2 on 2020-01-14 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_code', models.CharField(max_length=10)),
                ('product_price', models.CharField(max_length=10)),
            ],
        ),
    ]

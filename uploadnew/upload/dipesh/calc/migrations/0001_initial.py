# Generated by Django 2.2.8 on 2020-01-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('filepath', models.FileField(null=True, upload_to='files/', verbose_name='')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-05-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_cancalcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='fruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruits_name', models.CharField(max_length=100)),
            ],
        ),
    ]

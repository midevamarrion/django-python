# Generated by Django 4.2.3 on 2023-07-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventories', '0002_product_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=30)),
                ('quantity', models.PositiveIntegerField()),
                ('products', models.ManyToManyField(to='inventories.product')),
            ],
        ),
    ]

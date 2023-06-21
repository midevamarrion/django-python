# Generated by Django 4.2.1 on 2023-06-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.IntegerField()),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('customer_id', models.IntegerField()),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
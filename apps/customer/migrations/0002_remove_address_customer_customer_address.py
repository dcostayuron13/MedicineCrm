# Generated by Django 4.2.4 on 2023-09-01 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_address', to='customer.address'),
        ),
    ]

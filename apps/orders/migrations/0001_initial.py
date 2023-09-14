# Generated by Django 4.2.5 on 2023-09-14 05:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created On')),
                ('modified_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified On')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending', max_length=20)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('inventory', models.ManyToManyField(to='inventory.inventory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

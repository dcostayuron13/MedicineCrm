# Generated by Django 4.2.5 on 2023-09-26 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_inventory_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='type',
        ),
        migrations.AddField(
            model_name='inventory',
            name='amount',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Amount'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='category',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='ingredients',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ingredients'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='use',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Suggested Use'),
        ),
    ]

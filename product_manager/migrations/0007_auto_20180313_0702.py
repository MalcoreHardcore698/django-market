# Generated by Django 2.0.3 on 2018-03-13 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_manager', '0006_auto_20180313_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='attributes',
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(blank=True, null=True, to='product_manager.Attribute'),
        ),
    ]
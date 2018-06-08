# Generated by Django 2.0.3 on 2018-03-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_manager', '0011_auto_20180313_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('$', 'USD'), ('€', 'EUR'), ('₽', 'RUB')], default='$', max_length=3),
        ),
    ]

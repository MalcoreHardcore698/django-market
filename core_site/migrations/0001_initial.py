# Generated by Django 2.0.3 on 2018-03-12 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheBestProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_manager.Product')),
            ],
        ),
    ]

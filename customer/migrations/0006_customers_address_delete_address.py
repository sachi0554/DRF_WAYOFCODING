# Generated by Django 4.0.4 on 2022-05-27 09:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_address_remove_customers_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
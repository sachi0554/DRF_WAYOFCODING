# Generated by Django 4.0.4 on 2022-05-17 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_shipment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('customers_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='customer.customers')),
                ('address1', models.CharField(blank=True, max_length=150)),
                ('pincode', models.CharField(blank=True, max_length=120)),
            ],
            bases=('customer.customers',),
        ),
        migrations.RemoveField(
            model_name='customers',
            name='address',
        ),
    ]

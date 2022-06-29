# Generated by Django 4.0.3 on 2022-04-09 05:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_delivary_date',
            field=models.DateTimeField(default=datetime.timedelta(days=5), null=True),
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BalfinCouponGenerator', '0003_coupon_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]

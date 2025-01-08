# Generated by Django 5.1.2 on 2024-11-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BalfinCouponGenerator', '0002_coupon_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='status',
            field=models.CharField(choices=[('not active', 'Not Active'), ('active', 'Active'), ('used', 'Used')], default='not active', max_length=10),
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-26 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tally_app', '0003_alter_ledger_voucher_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='ledger_opening_bal',
            field=models.IntegerField(blank=True, default='Null'),
        ),
    ]
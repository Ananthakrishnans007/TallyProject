# Generated by Django 4.0.6 on 2022-08-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tally_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger_voucher',
            name='Debit',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]
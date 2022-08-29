# Generated by Django 4.0.6 on 2022-08-29 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tally_app', '0011_alter_closing_balance_closing_balance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LedgerMonths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Leger_Month_closing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Closing_balance', models.IntegerField(blank=True, default='', null=True)),
                ('type', models.CharField(max_length=225)),
                ('debit', models.IntegerField(blank=True, default='', null=True)),
                ('credit', models.IntegerField(blank=True, default='', null=True)),
                ('Ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally_app.ledger')),
                ('month', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally_app.ledgermonths')),
            ],
        ),
        migrations.CreateModel(
            name='TotalClosing_balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_Closing_balance', models.IntegerField(blank=True, default='', null=True)),
                ('type', models.CharField(max_length=225)),
                ('ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally_app.ledger')),
            ],
        ),
        migrations.DeleteModel(
            name='Closing_balance',
        ),
        migrations.AddField(
            model_name='ledger_voucher',
            name='month',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally_app.ledgermonths'),
        ),
    ]

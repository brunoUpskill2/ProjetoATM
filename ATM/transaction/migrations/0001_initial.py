# Generated by Django 4.2.5 on 2023-11-13 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('admininstrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('recipientIBAN', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('withdrawal_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transactiontype'),
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('receipt_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=512)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('atm_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admininstrator.atmmachine')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transactiontype')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.atmuser')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('entity', models.CharField(max_length=5)),
                ('reference', models.CharField(max_length=9)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('deposit_id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.bankaccount')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction')),
            ],
        ),
    ]

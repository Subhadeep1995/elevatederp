# Generated by Django 2.2 on 2019-09-22 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('customers', '0002_customer_company_name'),
        ('contracts', '0002_auto_20190922_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_code', models.CharField(max_length=10)),
                ('roundsman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_status', models.CharField(choices=[('P', 'Pending'), ('C', 'Completed')], default='P', max_length=1)),
                ('proposed_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('agreed_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('contract_url', models.CharField(max_length=200)),
                ('payment_mode', models.CharField(choices=[('M', 'Monthly'), ('B', 'Biannual'), ('A', 'Annual')], default='M', max_length=1)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('round_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.Area')),
            ],
        ),
    ]

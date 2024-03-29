# Generated by Django 2.2 on 2019-10-02 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateTimeField()),
                ('payment_status', models.CharField(choices=[('D', 'Due'), ('O', 'Overdue'), ('C', 'Complete')], default='D', max_length=1)),
                ('payment_completion_date', models.DateTimeField(auto_now=True)),
                ('amount_due', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='amount_due', to='contracts.Contract')),
                ('contract_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contract_id', to='contracts.Contract')),
            ],
        ),
    ]

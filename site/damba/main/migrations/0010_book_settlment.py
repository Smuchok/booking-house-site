# Generated by Django 3.2.7 on 2021-10-24 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settlment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_booking', models.DateTimeField()),
                ('date_of_settlment', models.DateTimeField()),
                ('date_of_checkout', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.clients')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.houses')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_booking', models.DateTimeField()),
                ('date_future_settlment', models.DateTimeField()),
                ('date_future_checkout', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.clients')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.houses')),
            ],
        ),
    ]

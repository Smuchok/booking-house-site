# Generated by Django 3.2.7 on 2021-10-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_price_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='pets_allow',
            field=models.BooleanField(default=False),
        ),
    ]

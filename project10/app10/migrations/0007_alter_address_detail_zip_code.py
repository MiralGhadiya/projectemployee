# Generated by Django 4.2.3 on 2023-07-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app10', '0006_alter_bank_bank_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address_detail',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]

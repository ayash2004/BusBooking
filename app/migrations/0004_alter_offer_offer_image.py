# Generated by Django 4.0.2 on 2022-02-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_image',
            field=models.ImageField(upload_to='offerimg'),
        ),
    ]
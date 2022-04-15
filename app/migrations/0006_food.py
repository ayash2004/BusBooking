# Generated by Django 4.0.2 on 2022-02-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('actual_price', models.IntegerField()),
                ('descriptions', models.TextField(max_length=300)),
                ('quantity', models.PositiveIntegerField()),
                ('food_image', models.ImageField(upload_to='foodimg')),
            ],
        ),
    ]

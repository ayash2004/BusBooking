# Generated by Django 4.0.2 on 2022-03-03 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_remove_ticket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2 on 2023-05-03 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0016_usercred_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonlocalouting',
            name='return_permitted',
            field=models.BooleanField(default=False),
        ),
    ]

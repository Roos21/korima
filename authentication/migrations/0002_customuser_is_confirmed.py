# Generated by Django 5.0.1 on 2024-01-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_confirmed",
            field=models.BooleanField(default=False),
        ),
    ]

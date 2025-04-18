# Generated by Django 5.1.3 on 2025-04-13 14:06
"""Initial migration"""

from django.db import migrations, models


class Migration(migrations.Migration):
    """Class to do the migration"""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CppExample",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.TextField()),
                ("status", models.CharField(max_length=100)),
                ("explanation", models.TextField()),
            ],
        ),
    ]

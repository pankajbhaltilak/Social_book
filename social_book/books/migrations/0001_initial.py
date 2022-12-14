# Generated by Django 4.1.1 on 2022-09-26 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
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
                ("file", models.FileField(blank=True, null=True, upload_to="")),
                ("file_name", models.CharField(max_length=254)),
                ("description", models.CharField(max_length=300)),
                ("visibility", models.BooleanField(default=True)),
                ("Cost", models.PositiveBigIntegerField(blank=True, null=True)),
            ],
        ),
    ]

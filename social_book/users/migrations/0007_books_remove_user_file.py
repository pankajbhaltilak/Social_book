# Generated by Django 4.1.1 on 2022-09-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_user_file_alter_user_roles"),
    ]

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
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="file",
        ),
    ]
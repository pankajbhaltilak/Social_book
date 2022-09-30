# Generated by Django 4.1.1 on 2022-09-23 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_roles"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="user",
            name="roles",
            field=models.CharField(
                choices=[("author", "Author"), ("seller", "Seller")],
                default="seller",
                max_length=10,
            ),
        ),
    ]

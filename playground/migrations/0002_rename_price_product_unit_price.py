# Generated by Django 5.0.1 on 2024-02-03 17:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("playground", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="price",
            new_name="unit_price",
        ),
    ]

# Generated by Django 4.1.1 on 2022-11-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MyApp", "0004_alter_recipe_difficulty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="time",
            field=models.PositiveIntegerField(
                help_text="Time to do this recipe in minutes"
            ),
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-28 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]

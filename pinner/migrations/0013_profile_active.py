# Generated by Django 3.2.7 on 2021-11-08 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinner', '0012_alter_profile_unliked'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 3.2.5 on 2021-09-06 04:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task0', '0006_alter_newuser_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
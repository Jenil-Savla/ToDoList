# Generated by Django 3.2.5 on 2021-09-06 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task0', '0007_task_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='profile_pic',
            field=models.ImageField(blank=True, default='./media/arcreactor.png', upload_to=''),
        ),
    ]

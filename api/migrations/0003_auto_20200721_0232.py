# Generated by Django 3.0.8 on 2020-07-21 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userwallet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

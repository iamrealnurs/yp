# Generated by Django 4.0.1 on 2022-02-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_seller_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='avatar',
            field=models.ImageField(blank=True, default='uploads/default.jpeg', null=True, upload_to='uploads/'),
        ),
    ]
# Generated by Django 4.0.1 on 2022-01-31 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_ads_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
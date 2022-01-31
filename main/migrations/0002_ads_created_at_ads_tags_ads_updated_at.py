# Generated by Django 4.0.1 on 2022-01-31 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.Tag'),
        ),
        migrations.AddField(
            model_name='ads',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

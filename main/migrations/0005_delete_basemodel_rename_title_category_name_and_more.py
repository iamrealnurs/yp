# Generated by Django 4.0.1 on 2022-01-31 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_basemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BaseModel',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='ads',
            name='title',
        ),
        migrations.AddField(
            model_name='ads',
            name='name',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
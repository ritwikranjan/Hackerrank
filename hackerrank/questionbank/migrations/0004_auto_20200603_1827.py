# Generated by Django 3.0.3 on 2020-06-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionbank', '0003_auto_20200603_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(),
        ),
    ]

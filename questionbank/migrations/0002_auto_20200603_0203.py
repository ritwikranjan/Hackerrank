# Generated by Django 3.0.3 on 2020-06-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionbank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_description',
            field=models.TextField(default='Description is a Must'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_link',
            field=models.TextField(),
        ),
    ]

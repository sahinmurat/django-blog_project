# Generated by Django 3.1.5 on 2021-01-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='number',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]

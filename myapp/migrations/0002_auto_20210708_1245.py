# Generated by Django 3.2.4 on 2021-07-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminar',
            name='counter',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='seminar_rating',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

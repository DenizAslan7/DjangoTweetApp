# Generated by Django 5.0 on 2023-12-15 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='message',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='tweet',
            name='nickname',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
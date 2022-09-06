# Generated by Django 4.0.6 on 2022-07-30 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0008_alter_news_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='answer_hotel',
        ),
        migrations.RemoveField(
            model_name='review',
            name='text_answer_hotel',
        ),
        migrations.AlterField(
            model_name='news',
            name='issued',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='review',
            name='issued',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='review',
            name='star',
            field=models.CharField(choices=[('ONE', '1'), ('TWO', '2'), ('THREE', '3'), ('FOUR', '4'), ('FIVE', '5')], max_length=10),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_category_news_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='favourite_site_review',
            field=models.BooleanField(default=False),
        ),
    ]

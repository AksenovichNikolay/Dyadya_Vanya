# Generated by Django 4.0.6 on 2022-07-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='call_back',
            name='test_field',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]

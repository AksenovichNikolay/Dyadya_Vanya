# Generated by Django 4.0.6 on 2022-07-29 20:14

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_category_news_category_name_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
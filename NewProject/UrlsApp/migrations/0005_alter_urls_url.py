# Generated by Django 4.2.4 on 2023-11-14 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrlsApp', '0004_alter_urls_options_remove_urls_title_urls_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='url',
            field=models.CharField(default='url', max_length=200, verbose_name='url'),
        ),
    ]
# Generated by Django 4.2.4 on 2023-11-14 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UrlsApp', '0003_alter_suburls_sub'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urls',
            options={'verbose_name': 'Url', 'verbose_name_plural': 'Urls'},
        ),
        migrations.RemoveField(
            model_name='urls',
            name='title',
        ),
        migrations.AddField(
            model_name='urls',
            name='name',
            field=models.CharField(default='name', max_length=100, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='urls',
            name='sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='UrlsApp.urls', verbose_name='корневой url'),
        ),
        migrations.AddField(
            model_name='urls',
            name='url',
            field=models.URLField(default='url', verbose_name='url'),
        ),
        migrations.DeleteModel(
            name='SubUrls',
        ),
    ]

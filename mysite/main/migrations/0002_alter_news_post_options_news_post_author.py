# Generated by Django 4.2.17 on 2025-01-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_post',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news_post',
            name='author',
            field=models.CharField(default='Unknown', max_length=50, verbose_name='Автор'),
        ),
    ]

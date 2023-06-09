# Generated by Django 4.2.1 on 2023-05-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_category_subscribers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcategory',
            name='subscribers',
        ),
        migrations.AlterField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category', verbose_name='Тематика'),
        ),
    ]

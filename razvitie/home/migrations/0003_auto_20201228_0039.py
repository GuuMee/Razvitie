# Generated by Django 3.1.4 on 2020-12-27 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201227_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('created',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
    ]

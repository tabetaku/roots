# Generated by Django 2.2.6 on 2019-10-30 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0002_auto_20191031_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.IntegerField(choices=[(0, '영화'), (1, '일본드라마')], verbose_name='작품 종류'),
        ),
    ]

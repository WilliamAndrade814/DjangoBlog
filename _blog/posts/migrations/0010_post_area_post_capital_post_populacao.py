# Generated by Django 4.1.1 on 2022-09-27 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='area',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='capital',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='populacao',
            field=models.TextField(default=''),
        ),
    ]

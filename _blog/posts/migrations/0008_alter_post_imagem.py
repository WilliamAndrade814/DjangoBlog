# Generated by Django 4.1.1 on 2022-09-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagem',
            field=models.URLField(blank=True, null=True),
        ),
    ]

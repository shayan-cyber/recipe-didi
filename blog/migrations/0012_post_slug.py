# Generated by Django 2.2.7 on 2020-05-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200520_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.7 on 2020-05-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200521_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno1', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('content', models.TextField()),
                ('emial', models.CharField(max_length=100)),
            ],
        ),
    ]

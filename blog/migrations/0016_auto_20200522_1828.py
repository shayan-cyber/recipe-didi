# Generated by Django 2.2.7 on 2020-05-22 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_contact_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emial',
            new_name='email',
        ),
    ]

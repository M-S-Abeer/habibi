# Generated by Django 2.0.2 on 2018-03-06 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solve_activities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solve',
            old_name='user',
            new_name='solver',
        ),
    ]

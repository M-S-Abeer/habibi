# Generated by Django 2.1.3 on 2019-06-05 09:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('badges', '0003_auto_20190605_1601'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='badgeacheiver',
            unique_together={('user', 'badge')},
        ),
    ]

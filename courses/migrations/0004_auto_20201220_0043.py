# Generated by Django 3.1.3 on 2020-12-19 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_courserequest_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserequest',
            name='status',
            field=models.CharField(default='waiting', max_length=256, verbose_name='status'),
        ),
    ]

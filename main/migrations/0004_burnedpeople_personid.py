# Generated by Django 4.2.7 on 2023-11-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_burnedpeople'),
    ]

    operations = [
        migrations.AddField(
            model_name='burnedpeople',
            name='PersonId',
            field=models.CharField(default='1', max_length=50),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-14 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageWork', '0003_auto_20200213_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mined_text',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]

# Generated by Django 4.2.11 on 2024-08-08 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0015_logentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='extra_field',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

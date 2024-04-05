# Generated by Django 4.2.8 on 2024-04-05 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dab_authentication', '0004_remove_authenticator_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticator',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, help_text='The user who created this resource', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='authenticator',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, help_text='The user who last modified this resource', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='authenticatormap',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, help_text='The user who created this resource', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='authenticatormap',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, help_text='The user who last modified this resource', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_modified+', to=settings.AUTH_USER_MODEL),
        ),
    ]

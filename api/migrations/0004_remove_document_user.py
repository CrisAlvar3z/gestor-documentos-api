# Generated by Django 3.2.5 on 2023-09-28 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_document_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='user',
        ),
    ]

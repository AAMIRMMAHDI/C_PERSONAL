# Generated by Django 4.2 on 2025-03-24 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0042_delete_resume'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='Stats',
        ),
    ]

# Generated by Django 4.2 on 2024-09-12 20:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name0', models.CharField(max_length=100)),
                ('name1', models.CharField(max_length=100)),
                ('name2', models.CharField(max_length=100)),
                ('name3', models.CharField(max_length=100)),
                ('name4', models.CharField(max_length=100)),
                ('name5', models.CharField(max_length=100)),
                ('scheduled', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField(default='test')),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]

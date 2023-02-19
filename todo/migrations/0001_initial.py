# Generated by Django 4.1.7 on 2023-02-19 09:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('task_added_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('task_updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

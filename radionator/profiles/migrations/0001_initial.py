# Generated by Django 3.1.4 on 2020-12-13 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(default='NoName', max_length=50)),
                ('background', models.CharField(choices=[('bg_1', 'Background 1'), ('bg_2', 'Background 2'), ('bg_3', 'Background 3'), ('bg_4', 'Background 4')], default='bg_1', max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2024-03-18 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SM', '0003_alter_scheduleentry_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleentry',
            name='period',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SM.lessontime'),
        ),
    ]

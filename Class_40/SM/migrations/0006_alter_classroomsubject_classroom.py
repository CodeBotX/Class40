# Generated by Django 4.2.7 on 2024-03-23 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SM', '0005_alter_classroomsubject_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroomsubject',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='SM.classroom'),
        ),
    ]
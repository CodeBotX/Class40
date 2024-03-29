# Generated by Django 4.2.6 on 2024-03-23 20:04

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LessonTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=10, unique=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TableSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayofweek', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable', to='SM.classroom')),
                ('period', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SM.lessontime')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='SM.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('school_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schoolyear', to='SM.schoolyear')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, null=True, size=None)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM.semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='SM.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM.subject')),
            ],
        ),
        migrations.CreateModel(
            name='ClassroomSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='SM.classroom')),
                ('subject', models.ManyToManyField(blank=True, to='SM.subject')),
            ],
        ),
    ]

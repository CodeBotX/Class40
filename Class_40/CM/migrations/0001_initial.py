# Generated by Django 4.2.6 on 2024-03-23 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SM', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.PositiveIntegerField()),
                ('column', models.PositiveIntegerField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='SM.classroom')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seat', to='SM.student')),
            ],
        ),
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('counter', models.PositiveIntegerField(default=1)),
                ('comment', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('grade', models.CharField(choices=[('T', 'Tốt'), ('K', 'Khá'), ('TB', 'Trung Bình'), ('Y', 'Yếu')], default='TB', max_length=2)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM.classroom')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

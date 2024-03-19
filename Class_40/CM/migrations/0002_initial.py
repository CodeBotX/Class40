# Generated by Django 4.2.6 on 2024-03-17 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CM', '0001_initial'),
        ('SM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='SM.classroom'),
        ),
        migrations.AddField(
            model_name='seat',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='SM.classroom'),
        ),
        migrations.AddField(
            model_name='seat',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Seat', to='CM.student'),
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CM.student'),
        ),
        migrations.AddField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM.subject'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM.classroom'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SM.subject'),
        ),
    ]
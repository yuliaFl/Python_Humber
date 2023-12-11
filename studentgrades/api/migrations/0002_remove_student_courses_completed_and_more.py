# Generated by Django 4.2.7 on 2023-12-08 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses_completed',
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses_enrolled',
        ),
        migrations.AddField(
            model_name='student',
            name='courses_completed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ongoingcourse'),
        ),
        migrations.AddField(
            model_name='student',
            name='courses_enrolled',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.completedcourse'),
        ),
    ]

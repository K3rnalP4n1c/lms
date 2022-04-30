# Generated by Django 4.0.4 on 2022-04-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_timetable_end_time_alter_timetable_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='class_type',
            field=models.CharField(choices=[('lecture', 'Lecture'), ('lab', 'Lab')], default='Lecture', max_length=7),
            preserve_default=False,
        ),
    ]
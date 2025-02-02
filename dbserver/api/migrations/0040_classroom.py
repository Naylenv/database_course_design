# Generated by Django 2.2.6 on 2019-12-09 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_remove_student_classroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroom_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Department')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
            },
        ),
    ]

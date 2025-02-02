# Generated by Django 2.2.6 on 2019-12-04 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_competition_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Act_Stu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Activity')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
            options={
                'verbose_name': '活动报名',
                'verbose_name_plural': '活动报名',
            },
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-05 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20191205_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='course',
            field=models.ForeignKey(blank=True, default='sd0030004', on_delete=django.db.models.deletion.CASCADE, to='api.Course'),
            preserve_default=False,
        ),
    ]
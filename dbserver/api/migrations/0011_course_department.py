# Generated by Django 2.2.6 on 2019-11-25 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20191125_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Department'),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.0.6 on 2018-07-10 11:59

import college.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20180705_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='myimg',
            field=models.ImageField(blank=True, null=True, upload_to='images\\', validators=[college.models.validate_img]),
        ),
    ]
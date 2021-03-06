# Generated by Django 2.0.6 on 2018-07-12 18:24

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('college', '0003_auto_20180710_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobno', models.IntegerField()),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='assignment',
            name='sem',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (0, 'All')], default=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator('^0?[6-9]{1}\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='rn',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
    ]

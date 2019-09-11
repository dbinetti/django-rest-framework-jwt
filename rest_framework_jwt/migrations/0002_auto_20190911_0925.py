# Generated by Django 2.2.4 on 2019-09-11 16:25

from django.db import migrations, models
import rest_framework_jwt.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_jwt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=100, validators=[rest_framework_jwt.validators.validate_punctuation]),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=100, validators=[rest_framework_jwt.validators.validate_punctuation]),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, validators=[rest_framework_jwt.validators.validate_punctuation]),
        ),
    ]

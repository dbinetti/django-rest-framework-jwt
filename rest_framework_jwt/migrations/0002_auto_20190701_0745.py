# Generated by Django 2.1.9 on 2019-07-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_jwt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, help_text='\n            The contact email of the resource.', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='family_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='given_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]

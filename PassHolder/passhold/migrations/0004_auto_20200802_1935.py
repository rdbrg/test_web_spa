# Generated by Django 3.0.8 on 2020-08-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passhold', '0003_auto_20200802_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='login',
            field=models.CharField(max_length=32, verbose_name='Login/Email'),
        ),
        migrations.AlterField(
            model_name='data',
            name='note',
            field=models.TextField(max_length=255, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='data',
            name='password',
            field=models.CharField(max_length=64, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=32, unique=True, verbose_name='Title'),
        ),
    ]

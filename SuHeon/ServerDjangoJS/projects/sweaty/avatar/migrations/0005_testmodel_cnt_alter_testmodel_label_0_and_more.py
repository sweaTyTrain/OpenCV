# Generated by Django 5.0.3 on 2024-03-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0004_testmodel_delete_testmode'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='cnt',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='label_0',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='label_1',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='label_2',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='label_3',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='label_4',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='label_5',
            field=models.CharField(default='default_value', max_length=100),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='label_6',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]

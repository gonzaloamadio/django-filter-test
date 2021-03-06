# Generated by Django 2.0 on 2018-12-29 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=512, verbose_name='biography'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Tester'), (2, 'Company')], null=True, verbose_name='type'),
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-17 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licenseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_comment',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
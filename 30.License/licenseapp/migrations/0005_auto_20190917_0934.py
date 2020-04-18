# Generated by Django 2.2.5 on 2019-09-17 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licenseapp', '0004_auto_20190917_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='license_detail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='licenseapp.LicenseDetail', verbose_name='詳細'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='software',
            name='software_name',
            field=models.CharField(max_length=128, unique=True, verbose_name='ソフト名'),
        ),
    ]
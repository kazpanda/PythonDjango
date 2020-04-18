# Generated by Django 2.2.5 on 2019-09-17 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licenseapp', '0003_licensedetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software_name', models.CharField(max_length=128, unique=True)),
                ('comment', models.CharField(max_length=500, verbose_name='コメント')),
            ],
            options={
                'verbose_name': 'ソフト名',
                'verbose_name_plural': 'ソフト名',
                'db_table': 'software',
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='language_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='licensedetail',
            name='software_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='licenseapp.Software', verbose_name='ソフト名'),
            preserve_default=False,
        ),
    ]

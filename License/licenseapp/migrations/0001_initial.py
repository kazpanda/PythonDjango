# Generated by Django 2.2.5 on 2019-09-16 21:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'カテゴリ',
                'verbose_name_plural': 'カテゴリ',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': '会社名',
                'verbose_name_plural': '会社名',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': '言語名',
                'verbose_name_plural': '言語名',
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='日付')),
                ('money', models.IntegerField(help_text='単位は日本円', verbose_name='金額')),
                ('memo', models.CharField(max_length=500, verbose_name='メモ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='licenseapp.Category', verbose_name='カテゴリ')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='licenseapp.Company', verbose_name='会社名')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='licenseapp.Language', verbose_name='言語名')),
            ],
            options={
                'verbose_name': 'ライセンス管理',
                'verbose_name_plural': 'ライセンス管理',
                'db_table': 'license',
            },
        ),
    ]

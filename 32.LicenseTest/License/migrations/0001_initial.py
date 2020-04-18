# Generated by Django 2.2.5 on 2019-10-06 04:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='M_Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'アプリケーション',
                'verbose_name_plural': 'アプリケーション',
                'db_table': 'm_application',
            },
        ),
        migrations.CreateModel(
            name='M_Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('base_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': '会社',
                'verbose_name_plural': '会社',
                'db_table': 'm_company',
            },
        ),
        migrations.CreateModel(
            name='M_Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': '言語',
                'verbose_name_plural': '言語',
                'db_table': 'm_language',
            },
        ),
        migrations.CreateModel(
            name='M_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('header', models.CharField(max_length=50, unique=True)),
                ('footer', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'メッセージ',
                'verbose_name_plural': 'メッセージ',
                'db_table': 'm_message',
            },
        ),
        migrations.CreateModel(
            name='M_RequestCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestcategory_name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': '申請区分',
                'verbose_name_plural': '申請区分',
                'db_table': 'm_requestcategory',
            },
        ),
        migrations.CreateModel(
            name='T_License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('display_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='表記番号')),
                ('hid', models.CharField(blank=True, max_length=30, null=True, verbose_name='HID')),
                ('remaining_point', models.IntegerField(blank=True, null=True, verbose_name='残ポイント')),
                ('memo', models.CharField(blank=True, max_length=100, null=True, verbose_name='メモ')),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='License.M_Application', verbose_name='アプリケーション名')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='License.M_Company', verbose_name='会社')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='License.M_Language', verbose_name='言語')),
            ],
            options={
                'verbose_name': 'ライセンス管理',
                'verbose_name_plural': 'ライセンス管理',
                'db_table': 't_license',
            },
        ),
        migrations.CreateModel(
            name='T_OperationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('starting_count', models.IntegerField(blank=True, null=True, verbose_name='起動回数')),
                ('weekly_report_count', models.IntegerField(blank=True, null=True, verbose_name='週報発行回数')),
                ('monthly_report_count', models.IntegerField(blank=True, null=True, verbose_name='月報発行回数')),
                ('memo', models.CharField(blank=True, max_length=200, null=True, verbose_name='メモ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='License.T_License', verbose_name='ライセンス管理')),
            ],
            options={
                'verbose_name': '使用履歴',
                'verbose_name_plural': '使用履歴',
                'db_table': 't_operation_history',
            },
        ),
        migrations.CreateModel(
            name='T_LicenseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('begin_date', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='開始日')),
                ('end_date', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='終了日')),
                ('mac_address', models.CharField(blank=True, max_length=20, null=True, verbose_name='MACアドレス')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='販売価格')),
                ('grant_point', models.IntegerField(blank=True, null=True, verbose_name='付与ポイント')),
                ('remaining_point', models.IntegerField(blank=True, null=True, verbose_name='残数ポイント')),
                ('renewal_deadline_notification', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新期限通知')),
                ('renewal_application_accepted', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新申請受理')),
                ('renewal_application_send', models.DateField(default=datetime.datetime.now, verbose_name='Key情報収集案内')),
                ('renewal_key_publish_notification', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='更新Key発行連絡')),
                ('discontinued_product_collection', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='廃止回収日')),
                ('memo', models.CharField(blank=True, max_length=200, null=True, verbose_name='メモ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='License.T_License', verbose_name='ライセンス管理')),
                ('request_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='License.M_RequestCategory', verbose_name='申請区分')),
            ],
            options={
                'verbose_name': 'ライセンス履歴',
                'verbose_name_plural': 'ライセンス履歴',
                'db_table': 't_history',
            },
        ),
    ]
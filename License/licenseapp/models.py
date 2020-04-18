from django.db import models
from datetime import datetime


# カテゴリーマスターテーブル
class Category(models.Model):

    class Meta:
        # テーブル名の指定
        db_table = "category"
        verbose_name = "カテゴリ"
        verbose_name_plural = "カテゴリ"
    # カラム名の定義
    category_name = models.CharField(max_length=255, unique=True)

    # ここから追加
    def __str__(self):
        return self.category_name


# 会社マスターテーブル
class Company(models.Model):

    class Meta:
        # テーブル名の指定
        db_table = "company"
        verbose_name = "会社名"
        verbose_name_plural = "会社名"
    # カラム名の定義
    company_name = models.CharField(
        verbose_name="会社名", max_length=128, unique=True)
    company_comment = models.CharField(
        verbose_name="コメント", max_length=255, blank=True)

    # ここから追加
    def __str__(self):
        return self.company_name


# 言語マスターテーブル
class Language(models.Model):

    class Meta:
        # テーブル名の指定
        db_table = "language"
        verbose_name = "言語名"
        verbose_name_plural = "言語名"
    # カラム名の定義
    language_name = models.CharField(max_length=50, unique=True)

    # ここから追加
    def __str__(self):
        return self.language_name


# ソフトマスターテーブル
class Software(models.Model):

    class Meta:
        # テーブル名の指定
        db_table = "software"
        verbose_name = "ソフト名"
        verbose_name_plural = "ソフト名"
    # カラム名の定義
    software_name = models.CharField(
        verbose_name="ソフト名", max_length=128, unique=True)
    comment = models.CharField(verbose_name="コメント", max_length=500, blank=True)

    # ここから追加
    def __str__(self):
        return self.software_name


# ライセンス詳細テーブル
class LicenseDetail(models.Model):

    class Meta:
        # テーブル名
        db_table = "license_detail"
        verbose_name = "ライセンス詳細"
        verbose_name_plural = "ライセンス詳細"
    # カラムの定義
    regist_date = models.DateField(verbose_name="登録日", default=datetime.now)
    begin_date = models.DateField(verbose_name="開始日", default=datetime.now)
    end_date = models.DateField(verbose_name="終了日", default=datetime.now)
    software_name = models.ForeignKey(
        Software, on_delete=models.PROTECT, verbose_name="ソフト名")
    serial_no = models.CharField(verbose_name="シリアルNO", max_length=128)
    price = models.IntegerField(verbose_name="販売金額", help_text="単位は日本円")
    grant_point = models.IntegerField(verbose_name="付与ポイント", default=0)
    remainingu_point = models.IntegerField(verbose_name="残ポイント", default=0)
    comment = models.CharField(verbose_name="コメント", max_length=500, blank=True)

    # ここから追加
    def __str__(self):
        return self.comment


# ライセンス管理テーブル
class License(models.Model):

    class Meta:
        # テーブル名
        db_table = "license"
        verbose_name = "ライセンス管理"
        verbose_name_plural = "ライセンス管理"
    # カラムの定義
    date = models.DateField(verbose_name="日付", default=datetime.now)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="カテゴリ")

    license_detail = models.ForeignKey(
        LicenseDetail, on_delete=models.PROTECT, verbose_name="詳細")

    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, verbose_name="会社名")

    language = models.ForeignKey(
        Language, on_delete=models.PROTECT, verbose_name="言語名")

    money = models.IntegerField(verbose_name="金額", help_text="単位は日本円")
    comment = models.CharField(verbose_name="コメント", max_length=500, blank=True)

    # ここから追加
    def __str__(self):
        return self.comment

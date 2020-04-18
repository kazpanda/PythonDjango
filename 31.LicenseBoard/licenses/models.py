import math
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe
from django.utils.text import Truncator
from markdown import markdown
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


# --------------------------------------------
# 言語マスターテーブル
# --------------------------------------------
class M_Language(models.Model):
    class Meta:
        # テーブル名の指定
        db_table = "m_language"
        verbose_name = "言語"
        verbose_name_plural = "言語"

    # 言語名
    language_name = models.CharField(max_length=20, unique=True)

    # 表示項目
    def __str__(self):
        return self.language_name


# --------------------------------------------
# 会社マスター
# --------------------------------------------
class M_Company(models.Model):
    class Meta:
        db_table = "m_company"
        verbose_name = "会社"
        verbose_name_plural = "会社"

    # 会社名
    company_name = models.CharField(max_length=100, unique=False)
    # 拠点名
    base_name = models.CharField(max_length=50, unique=True)

    # 表示項目
    def __str__(self):
        # 複数の項目を表示する
        return self.company_name + " : " + self.base_name


# --------------------------------------------
# アプリケーションマスター
# --------------------------------------------
class M_Application(models.Model):
    class Meta:
        db_table = "m_application"
        verbose_name = "アプリケーション"
        verbose_name_plural = "アプリケーション"

    # アプリケーション名
    application_name = models.CharField(max_length=50, unique=True)

    # 表示項目
    def __str__(self):
        return self.application_name


# --------------------------------------------
# メッセージマスターテーブル
# --------------------------------------------
class M_Message(models.Model):
    class Meta:
        db_table = "m_message"
        verbose_name = "メッセージ"
        verbose_name_plural = "メッセージ"

    message = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=50, unique=True)
    header = models.CharField(max_length=50, unique=True)
    footer = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.message


# --------------------------------------------
# 申請区分マスターテーブル
# --------------------------------------------
class M_RequestCategory(models.Model):
    class Meta:
        db_table = "m_requestcategory"
        verbose_name = "申請区分"
        verbose_name_plural = "申請区分"

    requestcategory_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.requestcategory_name


# --------------------------------------------
# ライセンス管理テーブル
# --------------------------------------------
class T_License(models.Model):
    class Meta:
        db_table = "t_license"
        verbose_name = "ライセンス"
        verbose_name_plural = "ライセンス"

    # 表示名
    display_name = models.CharField(max_length=30, unique=True)
    # HID
    hid = models.CharField(max_length=30, unique=True)
    # 記述
    memo = models.CharField(max_length=100)
    # 作成日
    created_at = models.DateTimeField(default=datetime.now)
    # 更新日
    updated_at = models.DateTimeField(auto_now=True)
    # 会社
    company = models.ForeignKey(M_Company, on_delete=models.PROTECT,
                                verbose_name="会社", null=True, blank=True)
    # 言語
    language = models.ForeignKey(M_Language, on_delete=models.PROTECT,
                                 verbose_name="言語", null=True, blank=True)
    # アプリケーション
    application = models.ForeignKey(M_Application, on_delete=models.PROTECT,
                                    verbose_name="アプリケーション名", null=True, blank=True)

    # 戻り文字
    def __str__(self):
        return self.display_name

    # Post数の取得
    def get_posts_count(self):
        return Post.objects.filter(topic__license=self).count()

    # Post更新日の取得
    def get_last_post(self):
        return Post.objects.filter(
            topic__license=self).order_by('-created_at').first()


# --------------------------------------------
# ライセンス発行テーブル
# --------------------------------------------
class T_Publication(models.Model):
    class Meta:
        db_table = "t_publication"
        verbose_name = "ライセンス発行履歴"
        verbose_name_plural = "ライセンス発行履歴"
    # 番号
    increment_num = models.AutoField(primary_key=True)
    # 作成日
    created_at = models.DateTimeField(default=datetime.now)
    # 記事
    # subject = models.CharField(max_length=255)
    # 更新日
    last_updated = models.DateTimeField(auto_now_add=True)
    # 閲覧数
    views = models.PositiveIntegerField(default=0)
    # 更新日
    updated_at = models.DateTimeField(auto_now=True)
    # 使用開始日
    begin_date = models.DateField(null=True, blank=True)
    # 使用終了日
    end_date = models.DateField(null=True, blank=True)
    # Macアドレス
    mac_address = models.CharField(max_length=20, null=True, blank=True)
    # 販売価格
    price = models.PositiveIntegerField(null=True, blank=True)
    # 付与ポイント
    grant_points = models.PositiveIntegerField(null=True, blank=True)
    # 残数ポイント
    remaining_point = models.PositiveIntegerField(null=True, blank=True)
    # 更新期限通知
    renewal_deadline_notification = models.DateField(null=True, blank=True)
    # 更新申請受理
    renewal_application_accepted = models.DateField(null=True, blank=True)
    # Key情報収集案内
    renewal_application_send = models.DateField(null=True, blank=True)
    # 更新Key発行連絡
    renewal_key_publish_notification = models.DateField(null=True, blank=True)
    # 廃止回収日
    discontinued_product_collection = models.DateField(null=True, blank=True)
    # メモ
    memo = models.CharField(max_length=100)
    # 外部Key
    license = models.ForeignKey(
        T_License, related_name='publications', on_delete=models.CASCADE)
    # 外部Key
    starter = models.ForeignKey(
        User, related_name='publications', on_delete=models.CASCADE)

    # 戻り値
    def __str__(self):
        return self.increment_num

    # ページ数の取得
    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)

    # 複数ページ確認の取得
    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    # ページ範囲の取得
    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)

    # 最終ページの取得
    def get_last_ten_posts(self):
        return self.posts.order_by('-created_at')[:10]


# --------------------------------------------
# 使用履歴テーブル
# --------------------------------------------
class T_Operation(models.Model):
    class Meta:
        db_table = "t_operation"
        verbose_name = "使用履歴"
        verbose_name_plural = "使用履歴"

    # 番号
    increment_num = models.AutoField(primary_key=True)
    # 作成日
    created_at = models.DateTimeField(default=datetime.now)
    # 更新日
    last_updated = models.DateTimeField(auto_now_add=True)
    # 更新日
    updated_at = models.DateTimeField(auto_now=True)
    # 起動回数
    starting_count = models.PositiveIntegerField(null=True, blank=True)
    # 週報発行回数
    weekly_report_count = models.PositiveIntegerField(null=True, blank=True)
    # 月報発行回数
    monthly_report_count = models.PositiveIntegerField(null=True, blank=True)
    # メモ
    memo = models.CharField(max_length=100)
    # 外部Key
    license = models.ForeignKey(
        T_License, related_name='operations', on_delete=models.CASCADE)
    # 外部Key
    starter = models.ForeignKey(
        User, related_name='operations', on_delete=models.CASCADE)

    # 戻り値
    # def __str__(self):
    #    return self.increment_num

    # ページ数の取得
    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)

    # 複数ページ確認の取得
    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    # ページ範囲の取得
    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)

    # 最終ページの取得
    def get_last_ten_posts(self):
        return self.posts.order_by('-created_at')[:10]

# --------------------------------------------
# Postテーブル
# --------------------------------------------


class Post(models.Model):
    message = models.TextField(max_length=100)
    topic = models.ForeignKey(
        T_Publication, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))


# https://hodalog.com/how-to-extend-django-user-model/


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    favorite_words = models.CharField(max_length=50, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

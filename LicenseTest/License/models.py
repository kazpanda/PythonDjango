from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# 言語マスターテーブル
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


# 会社マスター
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


# アプリケーションマスター
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


# メッセージマスターテーブル
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


# 申請区分マスターテーブル
class M_RequestCategory(models.Model):
    class Meta:
        db_table = "m_requestcategory"
        verbose_name = "申請区分"
        verbose_name_plural = "申請区分"

    requestcategory_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.requestcategory_name


# ライセンス管理テーブル
class T_License(models.Model):
    class Meta:
        # テーブル名
        db_table = "t_license"
        verbose_name = "ライセンス管理"
        verbose_name_plural = "ライセンス管理"

    # 外部キー
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name="作成者",
                               null=True,
                               blank=True)
    '''
    chenger = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                verbose_name="更新者")
    operator = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 verbose_name="使用者")
    responsible_person = models.ForeignKey(User,
                                           on_delete=models.CASCADE,
                                           verbose_name="責任者")
    '''
    company = models.ForeignKey(M_Company,
                                on_delete=models.PROTECT,
                                verbose_name="会社",
                                null=True,
                                blank=True)
    language = models.ForeignKey(M_Language,
                                 on_delete=models.PROTECT,
                                 verbose_name="言語",
                                 null=True,
                                 blank=True)
    application = models.ForeignKey(M_Application,
                                    on_delete=models.PROTECT,
                                    verbose_name="アプリケーション名",
                                    null=True,
                                    blank=True)
    # 自動フィールド
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # フィールド
    display_number = models.CharField(max_length=50,
                                      verbose_name="表記番号",
                                      null=True,
                                      blank=True)
    hid = models.CharField(max_length=30,
                           verbose_name="HID",
                           null=True,
                           blank=True)
    remaining_point = models.IntegerField(verbose_name="残ポイント",
                                          null=True,
                                          blank=True)
    memo = models.CharField(max_length=100,
                            verbose_name="メモ",
                            null=True,
                            blank=True)


# ライセンス履歴テーブル
class T_LicenseHistory(models.Model):
    class Meta:
        db_table = "t_history"
        verbose_name = "ライセンス履歴"
        verbose_name_plural = "ライセンス履歴"

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="作成者",
    )

    # 外部キー
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name="作成者")
    '''
    chenger = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                verbose_name="更新者")
    '''
    license = models.ForeignKey(T_License,
                                on_delete=models.PROTECT,
                                verbose_name="ライセンス管理")
    request_category = models.ForeignKey(M_RequestCategory,
                                         on_delete=models.PROTECT,
                                         verbose_name="申請区分")

    # 自動フィールド
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # フィールド
    begin_date = models.DateField(verbose_name="開始日",
                                  default=datetime.now,
                                  null=True,
                                  blank=True)
    end_date = models.DateField(verbose_name="終了日",
                                default=datetime.now,
                                null=True,
                                blank=True)
    mac_address = models.CharField(verbose_name="MACアドレス",
                                   max_length=20,
                                   null=True,
                                   blank=True)
    price = models.IntegerField(verbose_name="販売価格", null=True, blank=True)
    grant_point = models.IntegerField(verbose_name="付与ポイント",
                                      null=True,
                                      blank=True)
    remaining_point = models.IntegerField(verbose_name="残数ポイント",
                                          null=True,
                                          blank=True)
    renewal_deadline_notification = models.DateField(verbose_name="更新期限通知",
                                                     default=datetime.now,
                                                     null=True,
                                                     blank=True)
    renewal_application_accepted = models.DateField(verbose_name="更新申請受理",
                                                    default=datetime.now,
                                                    null=True,
                                                    blank=True)
    renewal_application_send = models.DateField(verbose_name="Key情報収集案内",
                                                default=datetime.now)
    renewal_key_publish_notification = models.DateField(
        verbose_name="更新Key発行連絡", default=datetime.now, null=True, blank=True)
    discontinued_product_collection = models.DateField(verbose_name="廃止回収日",
                                                       default=datetime.now,
                                                       null=True,
                                                       blank=True)
    memo = models.CharField(verbose_name="メモ",
                            max_length=200,
                            null=True,
                            blank=True)

    # 表示項目
    #def __str__(self):
    # 複数の項目を表示する
    #    return self.created_at.strftime('%Y/%m/%d') + " : " + self.author


# 使用履歴テーブル
class T_OperationHistory(models.Model):
    class Meta:
        db_table = "t_operation_history"
        verbose_name = "使用履歴"
        verbose_name_plural = "使用履歴"

    # 外部キー
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name="作成者")
    '''
    chenger = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                verbose_name="更新者")
    '''
    license = models.ForeignKey(T_License,
                                on_delete=models.PROTECT,
                                verbose_name="ライセンス管理")
    # 自動フィールド
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # フィールド
    starting_count = models.IntegerField(verbose_name="起動回数",
                                         null=True,
                                         blank=True)
    weekly_report_count = models.IntegerField(verbose_name="週報発行回数",
                                              null=True,
                                              blank=True)
    monthly_report_count = models.IntegerField(verbose_name="月報発行回数",
                                               null=True,
                                               blank=True)
    memo = models.CharField(verbose_name="メモ",
                            max_length=200,
                            null=True,
                            blank=True)

    # 表示項目
    def __str__(self):
        # 複数の項目を表示する
        return self.created_at.strftime('%Y/%m/%d')

from django.db import models

from django.utils import timezone

# Create your models here.
class Article(models.Model):
    """
    ブログ記事モデル
    """
    class Meta:
        # テーブル名を定義
        db_table = 'article'
    
    # テーブルのカラムに対応するフィールドを定義
    title = models.CharField(verbose_name = 'タイトル', max_length = 255)
    text = models.TextField(verbose_name = '本文', max_length = 2000)
    create_date = models.DateTimeField(verbose_name = '日時', 
                                       default = timezone.now)
    update_date = models.DateTimeField(verbose_name = '更新日時', 
                                       auto_now = True)
    
    def __str__(self):
        # データはオブジェクトのtitleを表示
        return self.title

class Category(models.Model):
    """
    ブログ記事のカテゴリ
    """
    class Meta:
        # テーブル名を定義
        db_table = 'category'

    # テーブルのカラムに対応するフィールドを定義
    article = models.OneToOneField(Article, verbose_name = '記事', 
                                  on_delete = models.CASCADE)
    ARTICLE_CHOICES = (
        ('programming', 'Programming'), 
        ('travel', 'Travel'), 
        ('workout', 'Workout')
    )
    genre = models.CharField(verbose_name = 'ジャンル', max_length = 50, 
                             choices = ARTICLE_CHOICES)
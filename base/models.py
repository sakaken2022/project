from django.db import models
# accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
    '''投稿するカテゴリを管理するモデル
    '''
    # カテゴリ名のフィールド
    title = models.CharField(
        verbose_name='カテゴリ', # フィールドのタイトル
        max_length=20)
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):カテゴリ名
        '''
        return self.title

class Post(models.Model):
    '''投稿されたデータを管理するモデル
    '''
    # CustomUserモデル(のuser_id)とPostモデルを
    # 1対多の関係で結び付ける
    # CustomUserが親でPostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
    # Categoryモデル(のtitle)とPostモデルを
    # 1対多の関係で結び付ける
    # Categoryが親でPostが子の関係となる
    category = models.ForeignKey(
        Category,
        # フィールドのタイトル
        verbose_name='カテゴリ',
        # カテゴリに関連付けられた投稿データが存在する場合は
        # そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    # タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=200        # 最大文字数は200
        )
    # コメント用のフィールド
    comment = models.TextField(
        verbose_name='コメント',  # フィールドのタイトル
        )
    
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True       # 日時を自動追加
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        
        Returns(str):投稿記事のタイトル
        '''
        return self.title

# Create your models here.
from django.db import models

class C_Program(models.Model):
    '''モデルクラス
    '''
    # カテゴリに設定する項目を入れ子のタプルとして定義
    # タプルの第1要素はモデルが使用する値、
    # 第2要素は管理サイトの選択メニューに表示する文字列

    # タイトルのフィールド
    title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=5        # 最大文字数は5
        )
    # サブタイトルのフィールド
    subtit = models.CharField(
        verbose_name='サブタイトル', # フィールドのタイトル
        max_length=30        # 最大文字数は30
        )
    # 問題文のフィールド
    content = models.TextField(
        verbose_name='問題文'   # フィールドのタイトル
        )
    # 問題プログラムのフィールド
    code = models.TextField(
        verbose_name='プログラム' # フィールドのタイトル
        )

    
    def __str__(self):
        '''Django管理サイトでデータを表示する際に識別名として
           投稿記事のタイトル(titleフィールドの値を表示するために必要
        
        Returns(str):投稿記事のタイトル
        '''
        return self.title
    
class Python_Program(models.Model):
    '''モデルクラス
    '''
    # カテゴリに設定する項目を入れ子のタプルとして定義
    # タプルの第1要素はモデルが使用する値、
    # 第2要素は管理サイトの選択メニューに表示する文字列

    # タイトルのフィールド
    title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=5        # 最大文字数は5
        )
    # サブタイトルのフィールド
    subtit = models.CharField(
        verbose_name='サブタイトル', # フィールドのタイトル
        max_length=30        # 最大文字数は30
        )
    # 問題文のフィールド
    content = models.TextField(
        verbose_name='問題文'   # フィールドのタイトル
        )
    # 問題プログラムのフィールド
    code = models.TextField(
        verbose_name='プログラム' # フィールドのタイトル
        )

    
    def __str__(self):
        '''Django管理サイトでデータを表示する際に識別名として
           投稿記事のタイトル(titleフィールドの値を表示するために必要
        
        Returns(str):投稿記事のタイトル
        '''
        return self.title

class Java_Program(models.Model):
    '''モデルクラス
    '''
    # カテゴリに設定する項目を入れ子のタプルとして定義
    # タプルの第1要素はモデルが使用する値、
    # 第2要素は管理サイトの選択メニューに表示する文字列

    # タイトルのフィールド
    title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=5        # 最大文字数は5
        )
    # サブタイトルのフィールド
    subtit = models.CharField(
        verbose_name='サブタイトル', # フィールドのタイトル
        max_length=30        # 最大文字数は30
        )
    # 問題文のフィールド
    content = models.TextField(
        verbose_name='問題文'   # フィールドのタイトル
        )
    # 問題プログラムのフィールド
    code = models.TextField(
        verbose_name='プログラム' # フィールドのタイトル
        )

    
    def __str__(self):
        '''Django管理サイトでデータを表示する際に識別名として
           投稿記事のタイトル(titleフィールドの値を表示するために必要
        
        Returns(str):投稿記事のタイトル
        '''
        return self.title

class Php_Program(models.Model):
    '''モデルクラス
    '''
    # カテゴリに設定する項目を入れ子のタプルとして定義
    # タプルの第1要素はモデルが使用する値、
    # 第2要素は管理サイトの選択メニューに表示する文字列

    # タイトルのフィールド
    title = models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=5        # 最大文字数は5
        )
    # サブタイトルのフィールド
    subtit = models.CharField(
        verbose_name='サブタイトル', # フィールドのタイトル
        max_length=30        # 最大文字数は30
        )
    # 問題文のフィールド
    content = models.TextField(
        verbose_name='問題文'   # フィールドのタイトル
        )
    # 問題プログラムのフィールド
    code = models.TextField(
        verbose_name='プログラム' # フィールドのタイトル
        )

    
    def __str__(self):
        '''Django管理サイトでデータを表示する際に識別名として
           投稿記事のタイトル(titleフィールドの値を表示するために必要
        
        Returns(str):投稿記事のタイトル
        '''
        return self.title
    
    
class Q_knowledge(models.Model):
    
    CATEGORY = (('basic','基礎問題',),
                ('advanced','応用問題'))
    
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    
    question = models.TextField(
        verbose_name='問題文'
        )
    
    select1 = models.CharField(
        verbose_name='選択１',
        max_length=200
        )
    
    select2 = models.CharField(
        verbose_name='選択2',
        max_length=200
        )
    
    select3 = models.CharField(
        verbose_name='選択3',
        max_length=200
        )
    
    select4 = models.CharField(
        verbose_name='選択4',
        max_length=200
        )
    
    select5 = models.CharField(
        verbose_name='選択5',
        max_length=200
        )
    
    answer = models.CharField(
        verbose_name='答え',
        max_length=200
        )
    
    def __str__(self):
        return self.title
    
class py_knowledge(models.Model):
     
     CATEGORY = (('basic','基礎問題',),
                 ('advanced','応用問題'))
     
     title = models.CharField(
         verbose_name='タイトル',
         max_length=200
         )
     
     question = models.TextField(
         verbose_name='問題文'
         )
     
     select1 = models.CharField(
         verbose_name='選択１',
         max_length=200
         )
     
     select2 = models.CharField(
         verbose_name='選択2',
         max_length=200
         )
     
     select3 = models.CharField(
         verbose_name='選択3',
         max_length=200
         )
     
     select4 = models.CharField(
         verbose_name='選択4',
         max_length=200
         )
     
     select5 = models.CharField(
         verbose_name='選択5',
         max_length=200
         )
     
     answer = models.CharField(
         verbose_name='答え',
         max_length=200
         )
     
     def __str__(self):
         return self.title
        
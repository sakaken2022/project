from django.contrib import admin
# CustomUserをインポート
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')

class PostAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')
  

# Django管理サイトにCategory、CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# Django管理サイトにPost、PostAdminを登録する
admin.site.register(Post, PostAdmin)



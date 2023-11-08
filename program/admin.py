from django.contrib import admin
# CustomUserをインポート
from .models import C_Program,Python_Program,Java_Program,Php_Program,Q_knowledge,py_knowledge

class C_ProgramAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')
  
class Python_ProgramAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')
    
class Java_ProgramAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')

class Php_ProgramAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')
  
class Q_knowledgeAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')
  
class py_knowledgeAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')
# Django管理サイトにBlogPost、BlogPostAdminを登録する

admin.site.register(C_Program, C_ProgramAdmin)

admin.site.register(Python_Program, Python_ProgramAdmin)

admin.site.register(Java_Program, Java_ProgramAdmin)

admin.site.register(Php_Program,Php_ProgramAdmin)

admin.site.register(Q_knowledge, Q_knowledgeAdmin)

admin.site.register(py_knowledge,py_knowledgeAdmin)

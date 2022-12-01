from django.contrib import admin
# CustomUserをインポート
from .models import Program,QuestionPost,KnowledgePost

class ProgramAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')


class QuestionPostAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')
  
class KnowledgePostAdmin(admin.ModelAdmin):
  '''管理ページのレコード一覧に表示するカラムを設定するクラス
  
  '''
  # レコード一覧にidとtitleを表示
  list_display = ('id', 'title')
  # 表示するカラムにリンクを設定
  list_display_links = ('id', 'title')
  
  

# Django管理サイトにBlogPost、BlogPostAdminを登録する
admin.site.register(Program, ProgramAdmin)

admin.site.register(QuestionPost, QuestionPostAdmin)

admin.site.register(KnowledgePost, KnowledgePostAdmin)
from django.urls import path
from . import views

# URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'program'

# URLパターンを登録するためのリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスが''(無し)の場合
    # viewsモジュールのindex_view()関数を実行
    # URLパターン名は'index'
    path('', views.learning_view, name='learning'),    
    # リクエストされたURLが「learn-detal/レコードのid/」の場合
    # viewsモジュールのlearn_detail()関数を実行
    # URLパターン名は'learn_detail'
    path(
        # 詳細ページのURLは「learn-detail/レコードのid/」
        'learn-detail/<int:pk>/',
        # viewsモジュールのlearn_detail()関数を実行
        views.learn_detail,
        # URLパターンの名前を'learn_detail'にする
        name='learn_detail'
        ),
    # Cカテゴリの一覧ページのURLパターン
    path(
        # Cカテゴリの一覧ページのURLは「C-list/」
        'C-list/',
        # viewsモジュールのC_view()関数を実行
        views.C_view,
        # URLパターンの名前を'C_list'にする
        name='C_list'
        ),
    # Pythonカテゴリの一覧ページのURLパターン
    path(
        # Pythonカテゴリの一覧ページのURLは「Python-list/」
        'Python-list/',
        # viewsモジュールのPython_view()関数を実行
        views.Python_view,
        # URLパターンの名前を'Python_list'にする
        name='Python_list'
        ),
    # Javaカテゴリの一覧ページのURLパターン
    path(
        # Cカテゴリの一覧ページのURLは「Java-list/」
        'Java-list/',
        # viewsモジュールのJava_view()関数を実行
        views.Java_view,
        # URLパターンの名前を'Java_list'にする
        name='Java_list'
        ),
    path(
        # ページのURLは「learning/」
        'c-programing/',
        # viewsモジュールのlearning_view()関数を実行
        views.learning_view,
        # URLパターンの名前を'learning'にする
        name='c-programing'
        ),
    path(
        # 詳細ページのURLは「learn-detail/レコードのid/」
        'select/',
        # viewsモジュールのlearn_detail()関数を実行
        views.select_view,
        # URLパターンの名前を'learn_detail'にする
        name='select'
        ),
]

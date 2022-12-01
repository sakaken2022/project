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
        'c-program/<int:pk>/',
        # viewsモジュールのlearn_detail()関数を実行
        views.C_detail,
        # URLパターンの名前を'learn_detail'にする
        name='C_detail'
        ),
    path(
        # ページのURLは「learning/」
        'c-list/',
        # viewsモジュールのlearning_view()関数を実行
        views.learning_view,
        # URLパターンの名前を'learning'にする
        name='C-list'
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

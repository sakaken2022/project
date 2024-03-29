from django.urls import path
from . import views

# URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'program'

# URLパターンを登録するためのリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスが''(無し)の場合
    # viewsモジュールのselect_view()関数を実行
    # URLパターン名は'select'
    path('', views.select_view, name='select'),    
    
    #----------問題の出題ページ-------------------------------------------
    
    path(
        # 詳細ページのURLは「C-detail/レコードのid/」
        'c-program/<int:pk>/',
        # viewsモジュールのC_detail()関数を実行
        views.C_detail,
        # URLパターンの名前を'C_detail'にする
        name='C_detail'
        ),
    path(
        # 詳細ページのURLは「Python-detail/レコードのid/」
        'python-program/<int:pk>/',
        # viewsモジュールのPython_detail()関数を実行
        views.Python_detail,
        # URLパターンの名前を'Python_detail'にする
        name='Python_detail'
        ),
    path(
        # 詳細ページのURLは「Java-detail/レコードのid/」
        'java-program/<int:pk>/',
        # viewsモジュールのJava_detail()関数を実行
        views.Java_detail,
        # URLパターンの名前を'Java_detail'にする
        name='Java_detail'
        ),
    path(
        # 詳細ページのURLは「PHP-detail/レコードのid/」
        'Php-program/<int:pk>/',
        # viewsモジュールのPHP_detail()関数を実行
        views.Php_detail,
        # URLパターンの名前を'PHP_detail'にする
        name='Php_detail'
        ),
    path(
        # 詳細ページのURLは「Java-detail/レコードのid/」
        'Q-program/<int:pk>/',
        # viewsモジュールのJava_detail()関数を実行
        views.Q_detail,
        # URLパターンの名前を'Java_detail'にする
        name='Q_detail'
        ),
    path(
        # 詳細ページのURLは「Java-detail/レコードのid/」
        'py-program/<int:pk>/',
        # viewsモジュールのJava_detail()関数を実行
        views.py_detail,
        # URLパターンの名前を'Java_detail'にする
        name='py_detail'
        ),
    #----------問題の選択ページ-------------------------------------------
    
    path(
        # ページのURLは「learning/」
        'c-list/',
        # viewsモジュールのlearning_view()関数を実行
        views.C_learning_view,
        # URLパターンの名前を'learning'にする
        name='C_list'
        ),
    path(
        # ページのURLは「learning/」
        'Python-list/',
        # viewsモジュールのlearning_view()関数を実行
        views.Python_learning_view,
        # URLパターンの名前を'learning'にする
        name='Python_list'
        ),
    path(
        # ページのURLは「learning/」
        'Java-list/',
        # viewsモジュールのlearning_view()関数を実行
        views.Java_learning_view,
        # URLパターンの名前を'learning'にする        
        name='Java_list'
        ),
    path(
        # ページのURLは「learning/」
        'Php-list/',
        # viewsモジュールのlearning_view()関数を実行
        views.Php_learning_view,
        # URLパターンの名前を'learning'にする
        name='Php_list'
        ),
    path(
        # ページのURLは「learning/」
        'Q-list/',
        # viewsモジュールのlearning_view()関数を実行
        views.Q_learning_view,
        # URLパターンの名前を'learning'にする
        name='Q_list'
        ),
    path(
        # ページのURLは「learning/」
        'py-list/',
        # viewsモジュールのlearning_view()関数を実行
        views.py_learning_view,
        # URLパターンの名前を'learning'にする
        name='py_list'
        ),
    #----------言語選択---------------------------------------------------
    
    path(
        # 問題の選択ページのURLは「select/」
        'select/',
        # viewsモジュールのselect_view()関数を実行
        views.select_view,
        # URLパターンの名前を'select'にする
        name='select'
        ),
]

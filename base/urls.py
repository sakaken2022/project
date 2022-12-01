from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'base'

# URLパターンを登録する変数
urlpatterns = [
    # アプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),
    
    # 投稿ページへのアクセスはviewsモジュールのCreatePostViewを実行
    path('post/', views.CreatePostView.as_view(), name='post'),
    
    # 投稿完了ページへのアクセスはviewsモジュールのPostSuccessViewを実行
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    
    # カテゴリ一覧ページ
    # stock/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('stock/<int:category>',
         views.CategoryView.as_view(),
         name = 'post_cate'
         ),

    # ユーザーの投稿一覧ページ
    # stock/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name = 'user_list'
         ),
    
    # 詳細ページ
    # post-detail/<postsテーブルのid値>にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('post-detail/<int:pk>',
         views.DetailView.as_view(),
         name = 'post_detail'
         ),
    
    # マイページ
    # mypage/へのアクセスはMypageViewを実行
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),

    # 投稿の削除
    # base/<postsテーブルのid値>/delete/にマッチング
    # <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('base/<int:pk>/delete/',
         views.DeleteView.as_view(),
         name = 'post_delete'
         ),
    # 問い合わせページのURLパターン
    path(
        # 問い合わせページのURLは「contact/」
        'contact/',
        # viewsモジュールのcontact_view()関数を実行
        views.contact_view,
        # URLパターンの名前を'contact'にする
        name='contact'
        ),
]


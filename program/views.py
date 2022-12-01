# Paginatorをインポート
from django.core.paginator import Paginator
# モデルProgramをインポート
from .models import Program
from django.shortcuts import render

def learning_view(request):
    '''トップページのビュー    
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルProgramのオブジェクトにorder_by()を適用して
    # Programのレコードを投稿日時の降順で並べ替える
    records = Program.objects.order_by('title')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 5)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', 1)
    # page()メソッドの引数にページ番号を設定し、
    # 該当ページのレコードを取得する
    pages = paginator.page(page_number)
    # render():
    # 第1引数: HTTPRequestオブジェクト
    # 第2引数: レンダリングするテンプレート
    # 第3引数: テンプレートに引き渡すdict型のデータ
    #         {任意のキー : リクエストされたページのレコードのリスト}
    return render(
        request, 'C-list.html', {'orderby_records': pages})

def C_detail(request, pk):
    '''詳細ページのビュー
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
      pk(int):
          投稿記事のレコードのid
    
    Returns(HTTPResponse):
        テンプレートbank.htmlをレンダリングした結果
    '''
    # モデルのマネージャーをProgram.objectsで参照し、get()を実行
    # 引数に指定したidのレコードを取得してrecordに格納
    record = Program.objects.get(id=pk)
    # render():
    # 第1引数: HTTPRequestオブジェクト
    # 第2引数: レンダリングするテンプレート
    # 第3引数: テンプレートに引き渡すdict型のデータ
    #         {任意のキー : get()で取得したレコード)}
    return render(
        request, 'C_pro.html', {'object': record})



def select_view(request):
    
    return render(
        request, 'select.html')


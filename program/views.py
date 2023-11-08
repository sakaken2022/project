# Paginatorをインポート
from django.core.paginator import Paginator
# モデルProgramをインポート
from .models import C_Program, Python_Program, Java_Program, Php_Program, Q_knowledge, py_knowledge
from django.shortcuts import render

def C_learning_view(request):
    '''トップページのビュー    
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルC_Programのオブジェクトにorder_by()を適用して
    # C_Programのレコードを投稿日時の降順で並べ替える
    records = C_Program.objects.order_by('title')
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
        request, 'C_list.html', {'orderby_records': pages})

def Python_learning_view(request):
    '''トップページのビュー    
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルPython_Programのオブジェクトにorder_by()を適用して
    # Python_Programのレコードを投稿日時の降順で並べ替える
    records = Python_Program.objects.order_by('title')
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
        request, 'Python_list.html', {'orderby_records': pages})

def Java_learning_view(request):
    '''トップページのビュー    
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルJava_Programのオブジェクトにorder_by()を適用して
    # Java_Programのレコードを投稿日時の降順で並べ替える
    records = Java_Program.objects.order_by('title')
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
        request, 'Java_list.html', {'orderby_records': pages})

def Php_learning_view(request):
    '''トップページのビュー    
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルPython_Programのオブジェクトにorder_by()を適用して
    # Python_Programのレコードを投稿日時の降順で並べ替える
    records = Php_Program.objects.order_by('title')
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
        request, 'Php_list.html', {'orderby_records': pages})

def Q_learning_view(request):
    '''トップページのビュー    
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルJava_Programのオブジェクトにorder_by()を適用して
    # Java_Programのレコードを投稿日時の降順で並べ替える
    records = Q_knowledge.objects.order_by('title')
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
        request, 'Q_list.html', {'orderby_records': pages})

def py_learning_view(request):
    '''トップページのビュー    
    テンプレートをレンダリングして戻り値として返す
    
    Parameters:
      request(HTTPRequest):
          クライアントからのリクエスト情報を格納したHTTPRequestオブジェクト
    
    Returns(HTTPResponse):
        render()でテンプレートをレンダリングした結果
    '''
    # モデルJava_Programのオブジェクトにorder_by()を適用して
    # Java_Programのレコードを投稿日時の降順で並べ替える
    records = py_knowledge.objects.order_by('title')
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
        request, 'py_list.html', {'orderby_records': pages})

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
    
    # モデルProgramのオブジェクトにorder_by()を適用して
    # Programのレコードを投稿日時の降順で並べ替える
    records = C_Program.objects.order_by('title')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 1)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', pk)
    # page()メソッドの引数にページ番号を設定し、
    # 該当ページのレコードを取得する
    pages = paginator.page(page_number)
    
    return render(
        request, 'C_pro.html', {'orderby_records': pages})

def Python_detail(request, pk):
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
    # モデルPython_Programのオブジェクトにorder_by()を適用して
    # Python_Programのレコードを投稿日時の降順で並べ替える
    records = Python_Program.objects.order_by('title')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 1)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', pk)
    # page()メソッドの引数にページ番号を設定し、
    # 該当ページのレコードを取得する
    pages = paginator.page(page_number)
    return render(
        request, 'Python_pro.html', {'orderby_records': pages})

def Java_detail(request, pk):
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
    # モデルJava_Programのオブジェクトにorder_by()を適用して
    # Java_Programのレコードを投稿日時の降順で並べ替える
    records = Java_Program.objects.order_by('title')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 1)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', pk)
    # page()メソッドの引数にページ番号を設定し、
    # 該当ページのレコードを取得する
    pages = paginator.page(page_number)
    return render(
        request, 'Java_pro.html', {'orderby_records': pages})

def Php_detail(request, pk):
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
    # モデルPython_Programのオブジェクトにorder_by()を適用して
    # Python_Programのレコードを投稿日時の降順で並べ替える
    records = Php_Program.objects.order_by('title')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 1)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', pk)
    # page()メソッドの引数にページ番号を設定し、
    # 該当ページのレコードを取得する
    pages = paginator.page(page_number)
    return render(
        request, 'Php_pro.html', {'orderby_records': pages})


def Q_detail(request, pk):
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
    # モデルJava_Programのオブジェクトにorder_by()を適用して
    # Java_Programのレコードを投稿日時の降順で並べ替える
    records = Q_knowledge.objects.order_by('title')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 1)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', pk)
    # page()メソッドの引数にページ番号を設定し、
    # 該当ページのレコードを取得する
    pages = paginator.page(page_number)
    return render(
        request, 'Q_pro.html', {'orderby_records': pages})


def py_detail(request, pk):
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
    # モデルJava_Programのオブジェクトにorder_by()を適用して
    # Java_Programのレコードを投稿日時の降順で並べ替える
    records = py_knowledge.objects.order_by('title')
    # Paginator(レコード, 1ページあたりのレコード数)でページに分割する
    paginator = Paginator(records, 1)
    # GETリクエストのURLにpageパラメーターがある場合はその値を取得する
    # pageパラメーターがない場合はデフォルトで1を返すようにする
    page_number  = request.GET.get('page', pk)
    # page()メソッドの引数にページ番号を設定し、
    # 該当ページのレコードを取得する
    pages = paginator.page(page_number)
    return render(
        request, 'py_pro.html', {'orderby_records': pages})


def select_view(request):
    
    return render(
        request, 'select.html')


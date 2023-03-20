import re
from django.shortcuts import render, redirect
# from django.views.decorators.csrf import crsf_emempt # @csrf_exempt 쓰려면
from .models import Article


# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 사용자 입력 받는 페이지 렌더링
def new(request):
    # new.html을 articles의 templates에 만들어서 가져오자!
    return render(request, 'articles/new.html')

# 입력 데이터를 처리하여 DB에 저장
# @csrf_exempt # csrf 함수를 제외시켜주세요
def create(request):
    # GET이 딕셔너리 형태로 가져와짐
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 인스턴스를 생성해서 DB에 저장(레코드 생성)
    # 2. 가장 대중적
    article = Article(title=title, content=content)
    print(article.created_at)
    print(article.updated_at)

    # 데이터베이스에 저장
    article.save()
    print(article.created_at)
    print(article.updated_at)

    # articles의 앱에 대한 가장 최상단에 있는 index를 가져온다..?
    # articles의 index path로 자동으로 이동
    return redirect('articles:index')
    # redirect(해당 페이지를 가도록) vs render(화면을 직접 만들어서??)

def details(request, pk):
    # pk값으로 데이터를 조회 (pk값은 variable routing으로 받은 정보)
    article = Article.objects.get(pk=pk)
    context = {'article' : article}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    # pk에 해당되는 게시판 글 하나 정보를 가져오기
    article = Article.objects.get(pk=pk)
    # 인스턴스. DB 레코드 삭제
    article.delete()
    return redirect('articles:index')

# 해당 게시물에 대한 정보를 조회하고
# 그 정보로 이루어진 입력 폼을 구성하겠다.
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

# 해당 게시글에 대한 정보 pk, 제목, 내용을 각각 가져와서 갱신
def update(request):
    # 해당 게시글에 대한 정보를 DB에서 가져온다
    # POST 딕셔너리에서 pk값 get
    pk = int(request.POST.get('pk'))
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    # 해당 게시글에 대한 상세페이지로 이동
    return redirect('articles:details', article.pk)
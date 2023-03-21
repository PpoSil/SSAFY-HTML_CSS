from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) # request.POST 데이터를 채우고 싶어
        if form.is_valid(): # 입력된 폼이 유효하다면
            article = form.save() # 알아서 연결되어 있는 모델을 가져와서 생성
            return redirect('articles:detail', article.pk)
    else: # 'GET'
        form = ArticleForm() # 비어있는 폼을 만들어

    context = {'form' : form}
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) # 비어있는 폼이 아닌, 유저의 정보를 채워야 함
        if form.is_valid(): # 입력된 폼이 유효하다면
            form.save() # article은 밖에 이미 있으므로 굳이 article.form~이렇게 안 해도 ok
            return redirect('articles:detail', pk=article.pk)

    else:
        form = ArticleForm(instance=article) # instance: 새로 만드는 것이 아닌 기존에 있는 정보 가져오기

    context = {'form': form}
    return render(request, 'articles/update.html', context)

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ArticlePost
from .forms import ArticlePostForm
# Create your views here.
from django.contrib.auth.models import User
import markdown


def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = {'articles':articles}
    # render函数：载入模板，并返回context对象
    return render(request,'article/list.html',context)
def article_detail(request,id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
    extensions = [
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
    ])
    context = {'article':article}
    return render(request,'article/detail.html',context)
def article_create(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("内容有误，请重新填写")
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form':article_post_form}
        return render(request,'article/create.html',context)
def article_delete(request,id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect("article:article_list")
def article_update(request,id):
    """
        更新文章的视图函数
        通过POST方法提交表单，更新titile、body字段
        GET方法进入初始表单页面
        id： 文章的 id
        """
    article = ArticlePost.objects.get(id=id)
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail",id=id)
        else:
            return HttpResponse("表单有误，请重新填写")

    else:
        article_post_form = ArticlePostForm()
        context = {'article':article,'article_psot_form':article_post_form}
        return render(request,'article/update.html',context)





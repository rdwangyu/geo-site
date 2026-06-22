from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Article

def index(request):
    articles = Article.objects.all()

    return render(
        request,
        "blog/index.html",
        {
            "articles": articles
        }
    )



def article_detail(request, slug):
    article = get_object_or_404(
        Article,
        slug=slug
    )

    return render(
        request,
        "blog/article.html",
        {
            "article": article
        }
    )

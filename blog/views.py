from django.shortcuts import render
from django.shortcuts import get_object_or_404
from pathlib import Path
from datetime import datetime
import markdown
import frontmatter


CONTENT_DIR = Path("content")


def index(request):

    articles = []

    for file in CONTENT_DIR.glob("*.md"):

        post = frontmatter.load(file)

        date = post.get("date")

        articles.append({
            "title": post.get("title"),
            "slug": post.get("slug"),
            "summary": post.get("summary"),
            "date": str(post.get("date")),
        })

    articles.sort(key=lambda x: x["date"], reverse=True)

    return render(request, "blog/index.html", {
        "articles": articles
    })


def article(request, slug):

    file_path = Path("content") / f"{slug}.md"
    post = frontmatter.load(file_path)
    md_content = post.content
    html = markdown.markdown(md_content)

    return render(request, "blog/article.html", {
        "title": post.get("title"),
        "date": post.get("date"),
        "summary": post.get("summary"),
        "content": html
    })


from datetime import datetime, timedelta

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.views import generic

from .config import PER_PAGE
from .models import Article, Author, Category


def my_render(request, template, kwargs):
    if 'categories' not in kwargs:
        kwargs['categories'] = Category.query_objects.all()
    if 'authors' not in kwargs:
        kwargs['authors'] = Author.query_objects.all()
    return render(request, template, kwargs)


class BaseDetailView(generic.DetailView):
    def render_to_response(self, context, **response_kwargs):
        context['categories'] = Category.query_objects.all()
        context['authors'] = Author.query_objects.all()
        return super().render_to_response(context, **response_kwargs)


def index_view(request):
    articles = Article.query_objects.all()[:PER_PAGE]
    return my_render(request, 'beeblog/index.html', {
        'articles': articles
    })


def list_recent_articles_view(request, days):
    now_time = datetime.now()
    start_day = now_time - timedelta(days=int(days))
    articles = Article.query_objects.filter(
        created__range=[start_day, now_time]).all()
    paginator = Paginator(articles, PER_PAGE)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return my_render(request, 'beeblog/list.html', {
        'page_objects': articles
    })


def list_category_article_view(request, category_id):
    articles = Article.query_objects.filter(categories__id=category_id).all()
    paginator = Paginator(articles, PER_PAGE)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return my_render(request, 'beeblog/list.html', {
        'page_objects': articles
    })


def list_author_article_view(request, author_id):
    articles = Article.query_objects.filter(author__id=author_id).all()
    paginator = Paginator(articles, PER_PAGE)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return my_render(request, 'beeblog/list.html', {
        'page_objects': articles
    })


def list_search_article_view(request):
    search_query = request.GET.get('search_query')
    articles = Article.query_objects.filter(
        title__icontains=search_query
    ).all()
    paginator = Paginator(articles, PER_PAGE)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return my_render(request, 'beeblog/list.html', {
        'page_objects': articles
    })


class DetailView(BaseDetailView):
    model = Article
    template_name = 'beeblog/detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

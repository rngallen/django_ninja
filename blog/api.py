from .schemas import ArticleIn, ArticleOut, UserSchema
from .models import Article
from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List

from django.contrib.auth import get_user_model
User = get_user_model()


router = Router()


@router.post('/articles/create')
def create_article(request, payload: ArticleIn):
    data = payload.dict()
    try:
        if not Article.objects.filter(title=data['title'], author=data['author']).exists():
            author = User.objects.get(id=data['author'])
            del data['author']
            article = Article.objects.create(author=author, **data)
            return {
                'detail': 'Article has been successfully created.',
                'id': article.id,
                'title': article.title,
            }
        else:
            return {'detail': f'Artilce with title {title} exists'}
    except User.DoesNotExist:
        return {'detail': 'The specific user cannot be found!'}


@router.get('/articles/{article_id}', response=ArticleOut)
def get_article(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    return article


@router.get('/articles', response=List[ArticleOut])
def get_articles(request):
    articles = Article.objects.all()
    return articles

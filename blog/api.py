from blog.schemas import ArticleIn, ArticleOut, UserSchema
from blog.models import Article
from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List

from django.contrib.auth import get_user_model
from django.db import router
User = get_user_model()


router = Router()


@router.post('/articles/create')
def create_article(request, payload: ArticleIn):
    data = payload.dict()
    try:
        author = User.objects.get(id=data['author'])
        del data['author']  # remove author from dictionary before unpacking it
        article = Article.objects.create(author=author, **data)
        return {
            'detail': 'Article has been successfully created.',
            'id': article.id,
            'title': article.title,
            'created': article.created,
        }
    except User.DoesNotExist:
        return {'detail': 'The specific user cannot be found!.'}


@router.get('/artilces/{article_id}', response=ArticleOut)
def get_article(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    return article


@router.get('/articles', response=List[ArticleOut])
def get_articles(request):
    artilces = Article.objects.all()
    return artilces

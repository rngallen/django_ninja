from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Article(models.Model):
    author = models.ForeignKey(User, verbose_name=_(
        "author"), on_delete=models.PROTECT)
    created = models.DateTimeField(_("timestamp"), auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    title = models.CharField(_("title"), max_length=500, unique=True)
    content = models.TextField(_("content"))

    def __str__(self):
        return f'{self.author.username}: {self.author.title}'

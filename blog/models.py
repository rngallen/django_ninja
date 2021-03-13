from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.PROTECT)
    title = models.CharField(_("title"), max_length=250)
    content = models.TextField(_("content"))
    created = models.DateTimeField(_("created"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True, auto_now_add=False)

    

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return f"{self.author.username}: {self.title}"

    # def get_absolute_url(self):
    #     return reverse("Article_detail", kwargs={"pk": self.pk})

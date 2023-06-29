from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from .utils import generate_random_string

# Create your models here.


class UrlShortner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    edit = models.DateTimeField(auto_now=True)
    url = models.URLField()
    url_key = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f"{self.short_url}"

    def __repr__(self):
        return f"< class UrlShortner [{self.created.strftime('%Y-%m-%d %H:%M:%S')}] [{self.user.username}] [{self.n_visits}] {self.url} {self.short_url}"

    def _gen_url_key(self) -> str:
        """
        Generate a random string of fixed length
        """
        urls = set(self.__class__.objects.all().values_list("url_key", flat=True))
        url_key = generate_random_string(getattr(settings, "SHORT_URL_LENGTH", 5))
        while url_key in urls:
            url_key = generate_random_string(getattr(settings, "SHORT_URL_LENGTH", 5))
        return url_key

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.url_key = self._gen_url_key()
        super().save(*args, **kwargs)

    @property
    def short_url(self):
        return f'{getattr(settings, "SHORT_URL_DEV_BASE" if settings.DEBUG else "SHORT_URL_BASE", "")}/{self.url_key}/'

    @property
    def n_visits(self):
        return self.visits.count()

    @property
    def last_visit(self):
        return self.visits.last()


class Visit(models.Model):
    url = models.ForeignKey(
        UrlShortner, on_delete=models.CASCADE, related_name="visits"
    )
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url.url} - {self.datetime.strftime('%Y-%m-%d %H:%M:%S')}"

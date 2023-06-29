from django.http import HttpResponseNotFound, HttpResponseRedirect
from threading import Thread

from main.models import UrlShortner, Visit

# Create your views here.


def create_visit(url):
    Visit.objects.create(url=url)


def index(request):
    return HttpResponseRedirect("/admin/")


def short_url(request, url_key):
    try:
        url = UrlShortner.objects.get(url_key=url_key)
        t = Thread(target=create_visit, args=(url,))
        t.start()
        return HttpResponseRedirect(url.url)
    except UrlShortner.DoesNotExist:
        return HttpResponseNotFound("Not found")

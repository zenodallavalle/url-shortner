from urllib.parse import parse_qs, urlsplit
from django.http import HttpResponseNotFound, HttpResponseRedirect
from threading import Thread
import re

from main.models import UrlShortner, Visit
from main.utils import create_redirect_url

# Create your views here.


def create_visit(url):
    Visit.objects.create(url=url)


def index(request):
    return HttpResponseRedirect("/admin/")


def short_url(request, url_key):
    splitted = urlsplit(request.get_full_path())
    params = parse_qs(splitted.query)
    fragment = splitted.fragment

    try:
        url = UrlShortner.objects.get(url_key=url_key)
        t = Thread(target=create_visit, args=(url,))
        t.start()
        destination_url = create_redirect_url(url.url, params, fragment)
        return HttpResponseRedirect(destination_url)
    except UrlShortner.DoesNotExist:
        return HttpResponseNotFound("Not found")

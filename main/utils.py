from string import ascii_lowercase, digits
from random import randint
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit


def generate_random_string(length=10):
    """
    Generate a random string of fixed length
    """
    # Choose from all lowercase letter
    letters = ascii_lowercase + digits
    return "".join([letters[randint(0, len(letters) - 1)] for _ in range(length)])


def extract_params_for_url(url):
    splitted = urlsplit(url)
    return dict(parse_qs(splitted.query))


def _merge_params(*parameters):
    ret = {}
    for params in parameters:
        for k, v in params.items():
            if k in ret:
                ret[k] += v
            else:
                ret[k] = v
    return ret


def create_redirect_url(long_url, params=dict(), fragment=""):
    splitted = urlsplit(long_url)

    url_params = extract_params_for_url(long_url)

    return urlunsplit(
        (
            splitted.scheme,
            splitted.netloc,
            splitted.path,
            urlencode(_merge_params(params, url_params), doseq=True),
            fragment,
        )
    )

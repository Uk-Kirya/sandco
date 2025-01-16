from django.http import HttpRequest, HttpResponse

from .models import Category


def context_all(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.filter(is_published=True).order_by('order')
    path_without_lang = request.path.split('/')[2:]
    path_without_lang = '/' + '/'.join(path_without_lang)

    context_all = {
        'categories': categories,
        'path_without_lang': path_without_lang,
    }

    return context_all
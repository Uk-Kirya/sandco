from django.http import HttpResponsePermanentRedirect


class DomainRedirect:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host().split(':')[0]
        if host.startswith('www.'):
            redirect_url = f"{request.scheme}://{host[4:]}{request.get_full_path()}"
            return HttpResponsePermanentRedirect(redirect_url)
        return self.get_response(request)

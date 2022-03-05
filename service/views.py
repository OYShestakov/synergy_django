from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world!')


def page(request, page_num):
    return HttpResponse(f'Page {page_num}')
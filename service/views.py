from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse

from .models import Product
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return HttpResponse('Hello world! on service')


def page(request, page_num):
    return HttpResponse(f'Page {page_num}')

def about(request, id):
    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404('Not found its my text')

    return HttpResponse('Ok')
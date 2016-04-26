from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
import datetime


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def current_datetime_render(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})


def display_meta(request):
    values = request.META.items()
    values.sort()
    return render(request, 'meta.html', {'metas': values})


# Higher-Level Abstractions of View Functions
def some_page(request):
    if request.method == 'POST':
        # do_something_for_post()
        return HttpResponseRedirect('/someurl/')
    elif request.method == 'GET':
        # do_something_for_get()
        return render(request, 'page.html')
    else:
        raise Http404()


# Higher-Level Abstractions of View Functions BETTER PRACTICE
def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404


def some_page_get(request):
    assert request.method == 'GET'
    # do_something_for_get()
    return render(request, 'page.html')


def some_page_post(request):
    assert request.method == 'POST'
    # do_something_for_post()
    return HttpResponseRedirect('/someurl/')


# Wrapping view functions
def requires_login(view):
    def new_view(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/')
        return view(request, *args, **kwargs)
    return new_view



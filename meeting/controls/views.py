#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhwei'

from django.views import generic
from django.http import Http404, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404

import models

class Index(generic.TemplateView):

    """
    Index
    """
    template_name = "index.html"

class Pages(generic.DetailView):

    template_name = "page.html"

    def get_context_data(self, **kwargs):
        context = super(Pages, self).get_context_data(**kwargs)
        context['page_list'] = models.Pages.objects.all()
        return context

    def get_object(self, queryset=None):
        try:
            mark = self.kwargs['page']
        except KeyError:
            raise Http404
        return get_object_or_404(models.Pages, mark=mark)

class RegisterMeeting(generic.CreateView):
    """
     注册会议
    """
    model = models.Members
    template_name = "register.html"
    success_url = '/'

    def get_success_url(self):
        messages.success(self.request, "注册成功！")
        return reverse_lazy("index")



class DownloadList(generic.ListView):

    model = models.Download
    template_name = "download.html"

    def get_context_data(self, **kwargs):
        context = super(DownloadList, self).get_context_data(**kwargs)
        context['page_list'] = models.Pages.objects.all()
        return context

def serve_file(request, file_id):

    obj = get_object_or_404(models.Download, id=file_id)
    response = HttpResponse(obj.document.file, content_type="")
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(obj.name.encode('utf-8'))
    return response
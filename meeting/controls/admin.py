#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhwei'

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

import models
import forms

class MemberAdmin(admin.ModelAdmin):

    list_display = ('name', 'sex', 'unit', 'duty')
    list_filter = ('sex', 'meeting_type','stay','created_date', 'payment')
    search_fields = ('name', )

admin.site.register(models.Members, MemberAdmin)



class DownloadAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'download_link', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'description', )
    form = forms.UploadFileForm

    fieldsets = (
        (None, {
            'fields': ('document', 'description')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('name',)
        }),
    )

    def download_link(self, obj):
        link = "<strong><a href={0}>下载</a></strong>".format(reverse('file',
                                       kwargs=dict(file_id=obj.id)))
        return mark_safe(link)
    download_link.short_description = "下载链接"

    def delete_model(self, request, obj):
        storage, path = obj.document.storage, obj.document.path
        super(DownloadAdmin, self).delete_model(request, obj)
        storage.delete(path)


admin.site.register(models.Download, DownloadAdmin)

class PageAdmin(admin.ModelAdmin):

    list_display = ('title', 'mark', 'updated_date','created_date',)

admin.site.register(models.Pages, PageAdmin)

admin.site.unregister(Site)
admin.site.unregister(Group)

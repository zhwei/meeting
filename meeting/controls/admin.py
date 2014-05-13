#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhwei'

from django.contrib import admin

import models

class MemberAdmin(admin.ModelAdmin):

    list_display = ('name', 'sex', 'unit', 'duty')

admin.site.register(models.Members, MemberAdmin)

class DownloadAdmin(admin.ModelAdmin):

    list_display = ('name', 'document')

admin.site.register(models.Download, DownloadAdmin)

class PageAdmin(admin.ModelAdmin):

    list_display = ('title', 'mark')

admin.site.register(models.Pages, PageAdmin)
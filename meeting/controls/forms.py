#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhwei'

from django import forms
import models

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = models.Download

    def save(self, commit=True):
        content = super(UploadFileForm, self).save(commit=False)
        content.name = self.cleaned_data['document'].name
        if commit: content.save()
        return content
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhwei'

import os
import uuid

from django.db import models
from ckeditor.fields import RichTextField


class TimeStampedModel(models.Model):
    """工具类
    用来给你的model添加下面两个字段，分别是创建时间和更新时间
    Usage: class YourModel(TimeStampedModel): ...
    """

    created_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        abstract = True


class Pages(TimeStampedModel):
    """
    Pages
    """

    title = models.CharField(verbose_name='标题', max_length=100)
    content = RichTextField(verbose_name='内容', config_name="default")

    mark = models.CharField(verbose_name='唯一标志', unique=True, max_length=20)

    class Meta:
        verbose_name = "页面"
        verbose_name_plural = "  页面"

    def __unicode__(self):
        return self.title




class Download(TimeStampedModel):
    """ Download Files
    """
    def upload_file_name(instance, filename):
        f, suffix = os.path.splitext(filename)
        return "files/{0}{1}".format(uuid.uuid4().hex, suffix)

    name = models.CharField(verbose_name='文件名', max_length=256, blank=True,
                            help_text="不要忘记添加后缀名")

    document = models.FileField(verbose_name='文件', upload_to=upload_file_name)

    description = models.TextField(verbose_name='文件描述')


    class Meta:
        verbose_name = '资料下载'
        verbose_name_plural = "资料下载"

    def get_file(self, id):

        return self.objects.get(id=id).document




class Members(TimeStampedModel):
    """ 参会成员资料
    """

    # Choices
    meeting_type_choices = (('teacher', '高校教师'), ('company', '企业'))
    stay_choices = (('standard', '标准间'), ('single', '单间'), ('self', '自行解决'))
    payment_choices = (('remit', '汇款'), ('cash', '现场交费（现金）'))

    name = models.CharField(verbose_name='姓名', help_text="必填", max_length=20)
    sex = models.CharField(choices=(('man', '男'), ('woman', '女')),
                           verbose_name="性别", max_length=10, default='man')

    meeting_type = models.CharField(verbose_name="参会类型", max_length=50, help_text="必填",
                                    choices=meeting_type_choices, default='teacher')

    unit = models.CharField(verbose_name='单位名称', max_length=100, help_text="必填")
    department = models.CharField(verbose_name='部门名称', max_length=100, help_text="必填")
    duty = models.CharField(verbose_name='职务', max_length=100, help_text="必填")

    email = models.EmailField(verbose_name="Email", help_text="必填")
    telephone = models.CharField(verbose_name="电话", max_length=13, help_text="必填")
    postcode = models.CharField(verbose_name="邮编", max_length=6, blank=True, null=True)

    stay = models.CharField(verbose_name="住宿类型", max_length=50, help_text="必填",
                            default='standard', choices=stay_choices)

    arrival_date = models.CharField(verbose_name="计划到达时间", max_length=50, help_text="必填")
    payment = models.CharField(verbose_name="缴费方式", max_length=10, help_text="必填",
                               default='remit', choices=payment_choices)
    payment_date = models.CharField(verbose_name="缴费时间", max_length=50, blank=True, null=True)

    need_bill = models.BooleanField(verbose_name="是否需要发票",
                                    choices=((True, '是'), (False, '否')), help_text="必填")
    bill_start = models.CharField(verbose_name="发票开头", max_length=100, blank=True, null=True)
    bill_address = models.CharField(verbose_name="发票邮寄地址", max_length=100,
                                    blank=True, null=True)

    class Meta:
        verbose_name = "参会成员"
        verbose_name_plural = "   参会成员"


    def __unicode__(self):
        return self.name

    def get_sex(self):
        return "男" if self.sex == "man" else "女"

    def get_choice_content(self, item, value):
        """ 获取choice的真实内容
        """
        return dict(self.__getattr__("{}_choices".format(item))).get(value, None)

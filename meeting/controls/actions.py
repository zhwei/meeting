#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhwei'

import datetime
from django.http import HttpResponse

COLUMNS = [(u"ID", 2000), (u"姓名", 2000), (u"Email", 8000), (u"性别", 1000),
            (u"电话", 6000), (u"参会类型", 4000),(u"单位名称", 8000),(u"部门名称", 6000),
           (u"职务", 6000), (u"邮编", 5000), (u"住宿类型", 4000), (u"计划到达时间", 6000),
           (u"缴费方式", 6000), (u"缴费时间", 6000),(u"是否需要发票", 4000), (u"发票开头", 6000),
           (u"发票邮寄地址", 6000),]

def get_row(obj):

    row = [ obj.id, obj.name, obj.email, obj.get_sex(),
            obj.telephone, obj.get_choice_content('meeting_type', obj.meeting_type),
            obj.unit, obj.department,
            obj.duty, obj.postcode, obj.get_choice_content("stay", obj.stay), obj.arrival_date,
            obj.get_choice_content("payment", obj.payment), obj.payment_date,
            obj.get_yn(obj.need_bill), obj.bill_start,
            obj.bill_address, ]
    return row

def get_fn():
    return "Export-XLS-{}".format(datetime.datetime.today().strftime('%Y-%m-%d'))


def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename={}.xls'.format(get_fn())
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("参会成员")

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(COLUMNS)):
        ws.write(row_num, col_num, COLUMNS[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = COLUMNS[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in queryset:
        row_num += 1
        row = get_row(obj)
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

export_xls.short_description = u"导出为XLS电子表格"

def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(get_fn())
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Title"),
        smart_str(u"Description"),
    ])
    for obj in queryset:
        writer.writerow([smart_str(i) for i in get_row(obj)])
    return response
export_csv.short_description = u"导出为CSV文件"
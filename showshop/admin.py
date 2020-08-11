from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from .models import shops,question
from .views import indexPage


@admin.register(shops)
class shopsAdmin(admin.ModelAdmin):

    list_display = ['upload_img', 'spname', 'spcount', 'spyujin',]  # 显示列
    #设置按商品名称查找
    search_fields = ['spname']  # 查找
    # 设置执行位置
    actions_on_top = False
    actions_on_bottom = True

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

@admin.register(question)
class questionAdmin(admin.ModelAdmin):
    list_display = ['upload_img','restype', 'rescontent', 'pass_audit_str']  # 显示列
    # 设置按商品名称查找
    search_fields = ['restype']  # 查找
    # 设置执行位置
    actions_on_top = False
    actions_on_bottom = True
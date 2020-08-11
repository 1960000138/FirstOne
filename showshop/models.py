from django.db import models

# Create your models here.
from django.utils.html import format_html


class shops(models.Model):
    spname = models.CharField(max_length=255)
    spimg = models.ImageField(upload_to="avatar/")
    spcount = models.IntegerField()
    spyujin = models.CharField(max_length=5)

    #admin显示图片
    def upload_img(self):
        return format_html(
            '<img src="{}" style="width:50px;height:50px;"/>',self.spimg.url,
        )
    #设置显示列名
    upload_img.short_description = 'Image'

    def __str__(self):
        return self.spname


class question(models.Model):

    restype = models.CharField(max_length=200,verbose_name="操作类型")
    spimgs = models.ImageField(upload_to='avatar/handleRquest/',verbose_name="商品图片")
    rescontent = models.CharField(max_length=255,verbose_name="商品ID")
    # admin显示图片
    def upload_img(self):
        return format_html(
            '<img src="{}" style="width:50px;height:50px;"/>', self.spimgs.url,1
        )

    # 设置显示列名
    upload_img.short_description = 'Image'
    def pass_audit_str(self):
        btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
                  '<input name="通过"' \
                  'type="button" id="passButton" ' \
                  'title="passButton" value="通过">' \
                  '</a>'
        return format_html(btn_str, '/deleShop?spId={}&ques={}'.format(self.rescontent,self.id))
    pass_audit_str.short_description = '是否通过审核'
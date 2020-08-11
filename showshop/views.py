from django.shortcuts import render
from django.shortcuts import redirect
from .models import shops as shop,question as ques
from django.http import HttpResponse, HttpResponseRedirect
import PIL.Image as Image
import os
# Create your views here.

def indexPage(request):
    try:
        shops = shop.objects.all()
        return render(request, 'index.html', {'shops': shops})
    except shop.DoesNotExist:
        return redirect('/indexPage')
#提交操作申请
def addQuestion(request):
    try:
        shops = shop.objects.get(id=request.GET.get('ids'))
        question = ques(restype='删除', spimgs=shops.spimg, rescontent=shops.id)
        question.save()
        return redirect('/admin/showshop/question/')
    except shop.DoesNotExist:
        return redirect('/indexPage')
#删除产品
def deleShop(request):
    spId = request.GET.get('spId')#获取需要删除商品的ID
    que = request.GET.get('ques')#操作申请ID
    try:
        shops = shop.objects.get(id=spId)
        shops.delete()
        quess = ques.objects.get(id=que)
        quess.delete()
    except shop.DoesNotExist:
        pass
    return redirect('/indexPage')

def rediaddShop(request):
    return render(request,'addshop.html')
#添加产品
def addShop(request):
    spname = request.GET.get('spname')
    spimg = request.GET.get('spimg')
    spcount = request.GET.get('spcount')
    spimg = '/avatar/{}'.format(spimg)
    shops = shop(spname=spname,spimg=spimg,spcount=spcount)
    shops.save()
    question = ques(restype='添加', spimgs=shops.spimg, rescontent=shops.id)
    question.save()
    return redirect('/indexPage')

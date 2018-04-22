# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import LiuYanKu
from django.views import View
from django.shortcuts import render
import time

# Create your views here.
class Index(View):
    def get(self,request):
        ly = LiuYanKu.objects.all()
        messtime = time.strftime('%Y-%m-%d %X',time.localtime())
        return render(request, 'message.html',locals())

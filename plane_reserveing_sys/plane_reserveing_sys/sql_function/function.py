from django.http import HttpResponse
from .forms import TravelerForm
from django.core.exceptions import ValidationError
import re

# Create your views here.
from django.shortcuts import render, redirect
from .forms import TravelerForm
from .models import Traveler

def traveler_create(request):
    if request.method == 'POST':
        form = TravelerForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)  # 打印清洗后的数据
            try:
                form.save()
                print("录入成功")
                return True
            except Exception as e:
                print(e)  # 打印异常信息
                return False
        else:
            print(form.errors)  # 打印表单错误
            return form.errors
    else:
        form = TravelerForm()
        return False



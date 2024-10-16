from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from plane_reserveing_sys.password_check import passwordcheck
from django.contrib import messages
from sql_function import function




def hello(request):
    return HttpResponse("Hello world ! ")

def login(request):

    if(request.method=='POST'):   
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        response,type=passwordcheck(username,password)
        if(response):
            print("登录成功"+str(type))
            if(type=='tours'):
                return redirect('http://127.0.0.1:8000/Tours_index/')
            if(type=='admin'):
                return redirect('http://127.0.0.1:8000/admin_index/')
        else:
            print("登录失败")
            messages.add_message(request, messages.ERROR, "账号或密码错误")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def admin_index(request):
    return render(request,'admin_index.html')

def Tours_index(request):
    if request.method=='POST':
        if function.traveler_create(request)==True:
            return render(request,'Tours_index.html')
        else:
        
            print(function.traveler_create(request))
            return render(request,'Tours_index.html')
    else:
        print("登录成功-用户类型：旅行社")
        return render(request,'Tours_index.html')


    
def regist(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'regist.html', context)


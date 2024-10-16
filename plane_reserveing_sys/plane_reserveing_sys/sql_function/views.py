from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import TravelerForm
from .models import Traveler

def traveler_create(request):
    if request.method == 'POST':
        form = TravelerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("录入成功")
            return redirect('success_url')  # 重定向到操作成功的页面
        else:
            return render(request, 'myapp/traveler_form.html', {'form': form})
    else:
        form = TravelerForm()
        return render(request, 'myapp/traveler_form.html', {'form': form})
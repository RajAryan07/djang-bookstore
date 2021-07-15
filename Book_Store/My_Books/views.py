from django.shortcuts import render
from . import forms
from My_Books.models import Form
from My_Books.filters import UserFilter


# Create your views here.

def Index(request):
    return render (request,'My_Books/index.html')

def Forms(request):
    form = forms.UserForm()

    if request.method == "POST":
        form = forms.UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return Show(request)
        else:
            print("Invalid Entry")
    return render (request,'My_Books/form.html',{'form':form})

def Show(request):
    form_list = Form.objects.all().order_by('-id')[:1]
    return render (request,'My_Books/show.html',{'uForm': form_list})

def Search(request):
    user_list = Form.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'My_Books/data.html',{'filter': user_filter})

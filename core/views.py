from django.contrib.auth import login

from django.shortcuts import render,redirect

from .forms import SingUpForm
# Create your views here.

def frontpage(request):
    return render(request , 'core/frontpage.html')

def singup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('frontpage')
    else:
        form = SingUpForm()

    return render (request,'core/singup.html',{'form':form})
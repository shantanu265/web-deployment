from django.shortcuts import render
from newapp.forms import UserForm

# Create your views here.

def index(request):
    return render(request,'base.html')


def register(request):
        registered = False,

        if request.method == 'POST':

                form = UserForm(data=request.POST)
                if form.is_valid():
                    user = form.save()
                    user.set_password(user.password)
                    user.save()
                    registered = True
                return render(request,'base.html')
        else :
            form = UserForm()
            return render(request,'index.html',{'form':form})



from django.shortcuts import render
from give.models import jacob
from .forms import Newuser
# Create your views here.
def index(request):
    dictt={'innerme':"go back"}
    return render(request,"usr.html",context=dictt)


def modf(request):
    form = Newuser()
    if request.method == 'POST':
        form =Newuser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("error")
    return render(request,"login.html",{'form':form})
#def moform(request):
#    form=FormName()
#
#    if request.method == 'POST':
#        form =FormName(request.POST)

        #do something code
#        if form.is_valid():
#            print('validation succesful')
#            print("Name:"+form.cleaned_data["name"])
#            print("Email:"+form.cleaned_data["email"])
#            print("TEXT:"+form.cleaned_data["text"])

#    return render(request,'formm.html',{'form':form})

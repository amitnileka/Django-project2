from django.shortcuts import render

# Create your views here.
def index(request):
    context_dic={'value':'AMIT NIL','age':20}
    return render(request,'index.html',context_dic)

def other(request):
    return render(request,'other.html')

def relative(request):
    return render(request,'relativeurl_template.html')

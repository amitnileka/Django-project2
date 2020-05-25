from django.shortcuts import render
from django.http import HttpResponse
from gogo.models import AcsessRecord,Topic,webpage

# Create your views here.
def amma(request):
    web_pages=AcsessRecord.objects.order_by('date')
    date_dictt={'inery':web_pages}
    return render(request,'amitnn.html',context=date_dictt)


def gamma(request):
    return HttpResponse("GO BACK BSDK")

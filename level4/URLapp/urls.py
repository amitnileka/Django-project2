from django.urls import path
from  URLapp import views


#Template tagging

app_name='URLapp'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name="other"),
]

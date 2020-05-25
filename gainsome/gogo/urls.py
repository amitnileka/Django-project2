from django.urls import re_path
from gogo import views

urlpatterns=[
re_path(r'^$',views.gamma,name='gamma')
]

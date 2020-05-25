from django.urls import path
from give import views

urlpatterns=[
    path('',views.modf,name="modf"),
]

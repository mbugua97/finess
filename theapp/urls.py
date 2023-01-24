from django.urls import path
from . import views

urlpatterns=[
    path('',views.pageone,name='pageone'),
    path('fogot/',views.login,name='fogot'),
    path('newuser/',views.newuser,name='newusers'),
]
from django.urls import path
from . import views

urlpatterns=[
    path('',views.billing,name='bill'),
    path('show',views.show,name='show'),
    path('cal/',views.calculation,name='cal')
]
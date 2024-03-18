from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('db1', views.db1, name='dashboard1'),
    path('db2', views.db2, name='dashboard2'),
    path('db3', views.db3, name='dashboard3'),
    path('db4', views.db4, name='dashboard4'),
    path('about', views.about, name='sobre'),
    path('faq', views.faq, name='faq'),
]
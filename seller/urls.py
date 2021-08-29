from django.urls import path
from . import views
urlpatterns=[path('', views.seller_login, name='sellerlogin'),
path('slogout', views.seller_logout, name='sellerlogout'),
path('ssignup', views.seller_signup, name='sellersignup'),
path('dashboard', views.dashboard, name='dashboard'),
path('addbook', views.addbook, name='addbook'),
path('delbook/<int:id>', views.delbook, name='deletebook'),
path('updbook/<int:id>', views.updbook, name='updatebook'),
path('detailc/<bname>/<uname>', views.detailcustomer, name='detail'),

]
from django.urls import path
from . import views
urlpatterns=[path('', views.customer_login, name='customerlogin'),
path('csignup', views.customer_signup, name='customersignup'),
path('dashboard', views.dashboard, name='customerdash'),
path('buybook/<int:id>', views.order, name='buybook'),
path('myorders', views.myorder, name='myorder'),
path('search', views.search, name='search'),
]
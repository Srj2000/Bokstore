from django.contrib import auth
from django.http.response import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout,authenticate
from .models import Customer
from django.shortcuts import render,redirect
from seller.models import Addbook
from .models import buyers
def customer_login(request):
    if     request.user.is_authenticated and request.user.groups.filter(name="customer"): 
        
        
        
        return redirect('/customer/dashboard')
        

    if request.method=="POST":
        uname=request.POST.get('uname')
        psk=request.POST.get('psk')
        user=authenticate(username=uname,password=psk)
        if user is not None:
            if user.groups.filter(name="customer"):
                login(request, user)
                return redirect('/customer/dashboard')
                print('success')

    return render(request, 'customer/login.html')


def customer_signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        psk1=request.POST.get('psk1')
        psk2=request.POST.get('psk2')
        add1=request.POST.get('add1')
        add2=request.POST.get('add2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        if psk1==psk2:
            myuser=User.objects.create_user(uname,email,psk1)
            myuser.first_name=name
            myuser.save()
            group=Group.objects.get(name='customer')
            group.user_set.add(myuser)
            custom=Customer(user=myuser,mobile=mobile,city=city, state=state,zip=zip,address1=add1,address2=add2)
            custom.save()
            return redirect('/customer')
    return render(request, 'customer/signup.html')
# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        book=Addbook.objects.all()
        return render(request, 'customer/dashboard.html', {'book':book})

def order(request, id):
    if request.user.is_authenticated:
        book=Addbook.objects.get(id=id)
        print(book)
        book.status=0
        book.save()
        buy=buyers(user=request.user,item=book.book_name, price=book.price,post_by=book.user)
        buy.save()
        return redirect('/customer/myorders')

def myorder(request):
    if request.user.is_authenticated:
        list=buyers.objects.filter(user=request.user)
        if len(list)==0:
            return render(request, 'customer/myorders.html', {'msg':'You Have No Any Completed Order'})
        return render(request, 'customer/myorders.html', {'list':list, 'status':True})

def search(request):
    if  request.user.is_authenticated and request.user.groups.filter(name="customer"):
        text=request.POST.get('search').lower()
        print(text)
        books=Addbook.objects.all()
        mysearch=[]
        for i in books:
            if (text in i.book_name.lower() or text in i.author.lower() or text in i.category.lower() or text in i.description.lower() ):
                mysearch.append(i)
        return render(request, 'customer/dashboard.html', {'book':mysearch}) 



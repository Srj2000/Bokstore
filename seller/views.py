from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout 
from .models  import Seller,Addbook
from customer.models import buyers, Customer
def seller_login(request):
    if request.user.is_authenticated and request.user.groups.filter(name="seller"):
       
            return redirect('/seller/dashboard')
    if request.method=="POST":
        uname=request.POST.get('uname')
        psk=request.POST.get('psk')
        user=authenticate(username=uname,password=psk)
        if user is not None:
            if user.groups.filter(name="seller"):
                login(request, user)
                return redirect('/seller/dashboard')
                print('success')

    return render(request, 'seller/login.html')

def seller_logout(request):
    logout(request)
    return redirect('/seller/')


def seller_signup(request):
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
            group=Group.objects.get(name='seller')
            group.user_set.add(myuser)
            seller=Seller(user=myuser,mobile=mobile,city=city, state=state,zip=zip,address1=add1,address2=add2)
            seller.save()
            return redirect('/seller')


    return render(request, 'seller/signup.html')


def addbook(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            bookn=request.POST.get('bname')
            category=request.POST.get('category')
            author=request.POST.get('author')
            desc=request.POST.get('desc')
            price=request.POST.get('price')
            
            add=Addbook( user=request.user, book_name=bookn, category=category, author=author, description=desc, price=price,   status=1)
            add.save()
            return redirect('/seller/dashboard')
        return render(request, 'seller/addbook.html')

    
def dashboard(request):
    if request.user.is_authenticated:
        booklist=Addbook.objects.filter(user=request.user)
        if len(booklist)==0:
            return render(request, 'seller/dashboard.html',{'msg':'Your Books List is Empty','status':False})
        else:
            return render(request, 'seller/dashboard.html',{'book':booklist,'status':True})
    return HttpResponse('Bad Request')

def delbook(request, id):
    if request.user.is_authenticated:
        book=Addbook.objects.get(id=id)
        book.delete()
        return redirect('/seller/dashboard')
    

def updbook(request, id):
    if request.user.is_authenticated:
        b=Addbook.objects.get(id=id)
        if request.method=="POST":
            bookn=request.POST.get('bname')
            category=request.POST.get('category')
            author=request.POST.get('author')
            desc=request.POST.get('desc')
            price=request.POST.get('price')
            book= {'book_name':bookn,'category':category,'author':author,'description':desc,'price':price}
            Addbook.objects.filter(id=id).update(**book)
            return redirect('/seller/dashboard')
        return render(request, 'seller/updatebook.html', {'detail':b})
        
        

def detailcustomer(request, bname , uname):
    if request.user.is_authenticated:
        detail=buyers.objects.get(item=bname , post_by=uname)
        
        return render(request, 'seller/detail.html', {'detail':detail})

    return HttpResponse('Bad Request')



# Create your views here.

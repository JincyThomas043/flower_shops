from django.shortcuts import render
from django.shortcuts import render,redirect
import os
import razorpay
from .forms import *
from datetime import datetime

# Create your views here.

from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
from.models import *
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
def show(request):
    return render(request,'index.html')


def home(request):
    return render(request,'index-1.html')

def about(request):
    return render(request,'who_we.html')

def shop(request):
    return render(request,'shop.html')

def service(request):
    return render(request,'index-2.html')
def ser(request):
    return render(request,'service.html')
def gallery(request):
    return render(request,'index-3.html')

def price(request):
    return render(request,'index-4.html')



def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')

def all(request):
    data = Productdetails.objects.all()

    return render(request, 'all.html', {'data': data})



def registration(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        phoneno=request.POST['phoneno']
        password=request.POST['password']
        cpassword = request.POST['cpassword']
        print(username)
        if password==cpassword:
            if Registration.objects.filter(email=email).exists() or Registration.objects.filter(username=username).exists():
                messages.info(request, "Email already Registered", extra_tags="signup")
                return redirect(registration)
            else:
                val = Registration.objects.create(username=username, email=email, phoneno=phoneno, password=password)
                val.save()
                messages.info(request, " User Registered Successfully", extra_tags="signup")
                return redirect(login)
        else:
            messages.info(request, "Password doesn't match", extra_tags="signup")
            return redirect(registration)

    return render(request, 'Registration_user.html')

def login(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        try:
            data=Registration.objects.get(username=u)
            if p==data.password:
                request.session['id']=u
                return redirect(user_home)
            else:
                messages.error(request,'incorrect password')
        except Exception:
            if u=='admin' and p=='admin':
                request.session['id1']=u
                return redirect(admin_page)
            else:
                messages.success(request,'Incorrect username and password')
    return render(request,'Login_project.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Registration.objects.get(email=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            # return render(request, 'emailsent.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'forgetpassword.html')

def reset_password(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    usr = Registration.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            password_reset.user.password=new_password
            password_reset.user.save()
            # password_reset.delete()
            return redirect(login)
    return render(request, 'reset.html',{'token':token})



def user_home(request):
    if 'id' in request.session:
        user=Registration.objects.get(username=request.session['id'])
        data=Productdetails.objects.all()
        l=[]
        l1=[]
        try:
            data1=Cart.objects.filter(user_details=user)
            for i in data1:
                l.append(i.product_details)
        except:
            pass
        try:
            wish=Wishlist.objects.filter(user_details=user)
            for i in wish:
                l1.append(i.product_details)
        except:
            pass

        return render(request,'userhome.html',{'data':user,'data1':data,'d1':data1,'d2':wish,'list':l})
    return redirect(login)
def view_user(request):
    user=Registration.objects.all()
    return render(request,'viewuser.html',{'data':user})

def admin_page(request):
    return render(request,'adminpage.html')

def loginabhi(request):
    return render(request,'loginabhi.html')
def rose(request):
    data=Productdetails.objects.filter(category='ROSE')
    return render(request,'rose.html',{'data':data})
def boque(request):
    details=Productdetails.objects.filter(category='BOQUE')
    return render(request,'boque.html',{'details':details})
def potflowers(request):
    deta=Productdetails.objects.filter(category='Pot Flowers')
    return render(request,'potflower.html',{'detail':deta})
def valentine(request):
    s=Productdetails.objects.filter(category='VALENTINE')
    return render(request,'valentine.html',{'d':s})
def stages(request):
    t=Productdetails.objects.filter(category='STAGES')
    return render(request,'stages.html',{'m':t})

def gifts(request):
    q=Productdetails.objects.filter(category='GIFTS')
    return render(request,'gifts.html',{'n':q})

def image_details(request,d):
    data = Productdetails.objects.filter(pk=d)
    return render(request,'imagedetails.html',{'data':data})
def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(login)
    return redirect(login)

def add_product(request):
    if request.method=='POST':
        product_name=request.POST['n1']
        product_price=request.POST['n2']

        product_image=request.FILES['n3']
        product_stock = request.POST['n5']
        description=request.POST['n4']
        category=request.POST['category']
        details=Productdetails.objects.create(product_name=product_name,product_price=product_price,product_image=product_image,product_stock=product_stock,category=category,description=description)
        details.save()
        messages.success(request,'Data Saved')
        return render(request,'addproduct.html')
    return render(request,'addproduct.html')

def display_product(request):
    details=Productdetails.objects.all()
    return render(request,'displayproduct.html',{'data':details})

def delete_product(requst,d):
    data=Productdetails.objects.filter(pk=d)
    data.delete()
    messages.success(requst,'Data deleted')
    return redirect(display_product)


def update_product(request,d):

        dt = Productdetails.objects.get(pk=d)

        if request.method == 'POST':
            e = edit_image(request.POST, request.FILES,instance=dt)
            if e.is_valid():
                e.save()
                messages.success(request, 'updated successfully')
                return redirect(display_product)
        e=edit_image(instance=dt)
        return render(request, 'update.html', {'data2': e})


def add_cart(request,pid):
    if 'id' in request.session:
        user=Registration.objects.get(username=request.session['id'])
        data=Productdetails.objects.get(pk=pid)
        cart_details=Cart.objects.create(user_details=user,product_details=data,)
        cart_details.save()
        messages.success(request,'cart added succesfully')
        return redirect(user_home)
    return redirect(login)

def display_cart(request):
    if 'id' in request.session:
        data=Registration.objects.get(username=request.session['id'])
        user=Cart.objects.filter(user_details=data)
        qty=1
        total=0
        c=0
        for i in user:
            print(i.product_details.product_price)
            c=c+1
            total +=i.product_details.product_price*i.quantity
            print(total)
        return render(request,'cart.html',{'key':user,'tota':total})
    return HttpResponse("cart added succesfully")
def delete_from_cart(request,d):
    data=Cart.objects.filter(pk=d)
    data.delete()
    messages.success(request,'removed from cart')
    return redirect(display_cart)

def display_wishlist(request,pid):
    if 'id' in request.session:
        user=Registration.objects.get(username=request.session['id'])
        product=Productdetails.objects.get(pk=pid)
        if Wishlist.objects.filter(product_details_id=pid).exists():
            messages.error(request, 'Already Added in wishlist')
        else:
            cartdetails=Wishlist.objects.create(user_details=user,product_details=product)
            cartdetails.save()
            messages.success(request,'added to wishlist')
            return redirect(user_home)
    return redirect(user_home)

def wishlist(request):
    user_name=Registration.objects.get(username=request.session['id'])
    userdetails=Wishlist.objects.filter(user_details=user_name)
    return render(request,'wishlist.html',{'key':userdetails})

def remove_wishlist(request,d):
    data=Wishlist.objects.filter(pk=d)
    data.delete()
    messages.success(request,'removed from wishlist')
    return redirect(wishlist)
def increment_quantity(request,cart_id):
    cart_item=Cart.objects.get(pk=cart_id)
    if cart_item.product_details.product_stock>0:
        cart_item.quantity+=1
        cart_item.save()
        cart_item.total_price=cart_item.quantity*cart_item.product_details.product_price
        cart_item.save()

    return redirect(display_cart)

def decrement_quantity(request,cart_id):
    cart_item=Cart.objects.get(pk=cart_id)
    if cart_item.quantity>1:
        cart_item.quantity-=1
        cart_item.save()
    return redirect(display_cart)
def details(request,d):
    f = Productdetails.objects.get(pk=d)
    if request.method == "POST":
        s=Registration.objects.get(username=request.session['id'])
        if d:

            amount=f.product_price
            Fullname=request.POST['name']
            Pincode=request.POST['pincode']
            state=request.POST['state']
            Address= request.POST['address']
            city=request.POST['city']
            user=deliverydetails.objects.create(Fullname=Fullname,Pincode=Pincode,state=state,Address=Address,city=city,userdetails=s,productdetails_2=f,total_price=amount,payment_status='TRUE')
            user.save()
            f.product_stock = f.product_stock - 1
            f.save()
            messages.success(request, 'payment succuessfull')
            return redirect('pay',amount)

    else:
        user1= Registration.objects.get(username=request.session['id'])
        return render(request,"shippingdetails.html",{"user1":user1,"item":f})

def pay(request,amount):
    print(amount)
    amount = int(amount) * 100
    order_currency = 'INR'
    client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    return render(request, "pay.html",{'amount':amount})

def placeorder(request,amount):
    print(amount)
    print("hello")
    amount = int(amount) * 100
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))

    return render(request, "pay1.html",{'data1':amount})

def success_page(request):

    return render(request,"success_page.html")

def checkoutcart(re,total):
    user = Registration.objects.get(username=re.session['id'])
    print(user,"User")
    pro=Cart.objects.filter(user_details=user)
    print(pro)
    order_ids = []
    if re.method == 'POST':
        a = re.POST.get('user_name')
        c = re.POST.get('user_address')
        d = re.POST.get('user_city')
        e = re.POST.get('user_state')
        g = re.POST.get('user_zipcode')
        h = re.POST.get('user_phone')
        l = int(re.POST.get('user_total'))
        for i in pro:
            cn = i.product_details
            cq = i.quantity
            ct = i.product_details.product_price * i.quantity
            v=deliverydetails(userdetails=user, Fullname=a, Address=c, city=d, state=e, Pincode=g, productdetails_2=cn,quantity=cq,total_price=ct,)
            v.save()
            de=Cart.objects.filter(product_details=cn)
            de.delete()
            value1 = v.pk
            order_ids.append(value1)
            Productdetails.objects.filter(pk=i.product_details.pk).update(product_stock=i.product_details.product_stock - cq)
        re.session['order_ids'] = order_ids
        return redirect(payment_cart,l)
    return render(re,'checkout_cart.html',{'user':user,'data':pro,'total':total})
def payment_cart(request, l):
    amount = l* 100
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, "payment_cart.html",{'amount':amount})

def userrecentorders(re):
    if 'id' in re.session:
        user = Registration.objects.get(username=re.session['id'])
        order = deliverydetails.objects.filter(userdetails=user,payment_status='TRUE').order_by('-purchase_date')
        print(order)
        return render(re, 'user_recent_order.html',{'data':order})
    return redirect(login)

def profile(re):
    if 'id' in re.session:
        data = Registration.objects.get(username=re.session['id'])
        return render(re,'userprofile.html',{'data':data})
    return redirect(login)

def updateprofile(re):
    if 'id' in re.session:
        if re.method == 'POST':
            b = re.POST['phoneno']
            c = re.POST['email']
            d = re.POST['username']
            Registration.objects.filter(username=re.session['id']).update( phoneno=b, email=c, username=d)
            messages.success(re,'Profile Updated')
        return redirect(profile)

def changepassword(request):
    if 'id' in request.session:
        if request.method == 'POST':
            a = request.POST.get('current_password')
            b = request.POST.get('new_password')
            c = request.POST.get('confirm_password')
            try:
                data = Registration.objects.get(username=request.session['id'])
                if data.password == a:
                    if b == c:
                        Registration.objects.filter(username=request.session['id']).update(password=b)
                        messages.success(request, 'Password Updated')
                        return redirect(profile)
                    else:
                        messages.error(request, 'Passwords Do not Match')
                        return redirect(profile)
                else:
                    messages.error(request, 'Password Incorrect')
                    return redirect(profile)
            except Exception:
                return redirect(profile)

def low_stock(re):
    # if 'admin' in re.session:
        a = Productdetails.objects.all()

        l=[]
        for i in a:
            if i.product_stock < 5:
                l.append(i)
                # print(i.Stock)
        print("l",l)
        return render(re,'lowstock.html',{'item':l})

def payment_success_cart(request):
    if 'id' in request.session:
        user = Registration.objects.get(username=request.session['id'])
        order_ids = request.session.get('order_ids', [])
        for i in order_ids:
            c = i
            b = 'PAID'
            deliverydetails.objects.filter(pk=c).update(payment_status=b)
        send_mail('Payment Successful',
                  f'Hey {user.username}, Your payment was successful and your ordered items has been successfully placed. \nWe are working on your order. \nOrder status will be updated soon.\n\nTHANK YOU.. \n\nBest regards,\nGAMER ZONE',
                  'settings.EMAIL_HOST_USER', [user.email], fail_silently=False)

        send_mail('Out of Stock',
                  f' {c}, has placed a some new orders\nPlease review and update the order status',
                  'settings.EMAIL_HOST_USER', ['jinctj04@gmail.com'], fail_silently=False)
        return render(request, "success_page.html")
    return redirect(login)

def admin_orders(re):
    if 'id' in re.session:
        order = deliverydetails.objects.all()
        return render(re, 'adminorderdetails.html',{'data':order})
    return redirect(admin_page)

def adminorderupdate(request,d):
    if 'id' in request.session:
        ord = deliverydetails.objects.get(pk=d)
        print(ord)
        if request.method == 'POST':
            a = request.POST.get('odsts')
            b = request.POST.get('inst')
            deliverydetails.objects.filter(pk=d).update(product_status=a, instruction=b)
            return redirect(admin_orders)
        return render(request,'adminorderupdate.html',{'data':ord})
    return redirect(login)

def Search(p):
    if p.method=='POST':
        s=p.POST['search']
        data3=Productdetails.objects.filter(product_name=s)
        return render(p,'search.html',{'date':data3})
    return render(p,'search.html')
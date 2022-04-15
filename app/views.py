from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from . models import Cart, Contact, Food, Ticket,Offer,Profile, Register_table
from django.contrib import messages
from .forms import TicketForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from datetime import date
from django.contrib.sessions.backends.db import *

# Create your views here.

# def home(request):
#     return render(request, 'app/home.html')

class home(View):
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    def get(self,request):
        offers = Offer.objects.all()
        foods = Food.objects.all()
        return render(request, 'app/home.html',{'offers':offers,'foods':foods})


class Offer_details(View):
    def get(self, request, pk):
        offer = Offer.objects.get(pk=pk)
        return render(request,'app/offer_details.html',{'offer':offer})

class Food_details(View):
    def get(self, request, pk):
        food = Food.objects.get(pk=pk)
        return render(request,'app/food_details.html',{'food':food})

def signup(request):
    if request.method == 'POST':
        un = request.POST['username']
        fn = request.POST['fname']
        ln = request.POST['lname']
        en = request.POST['email']
        cn = request.POST['contact_number']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # Password VAlidation Code here
        #Contact No Validation code
        #Hover effect on Signup and Signin Button
        if fn.isalpha():
            pass
        else:
            messages.error(request,'First name field must contain alphabets')
            return redirect('signup') 

        if pass1 != pass2:
            messages.error(request,'Passwords does not match')
            return redirect('signup')
        elif User.objects.filter(email=en):
            messages.error(request,'Email already exists')
            return redirect('signup')
        elif User.objects.filter(username=un):
            messages.error(request,'Username already exists')
            return redirect('signup')
        elif len(cn)!=10:
            messages.error(request,'Phone Number Must contain 10 digits')
            return redirect('signup')
        else:
            usr = User.objects.create_user(un,en,pass1)
            usr.first_name = fn
            usr.last_name = ln
            usr.save()
            reg = Register_table(user=usr,contact_number=cn)
            reg.save()
            return render(request,'app/signin.html',{"status":"Dear {} your account created successfully".format(fn)})

    return render(request,'app/signup.html')

def signin(request):
    if request.method == 'POST':
        un = request.POST['username']
        pwd = request.POST['pass1']
        user = authenticate(username=un,password=pwd)
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin")
            else:
                return HttpResponseRedirect("/")
        else:
            messages.error(request,'Username or password incorrect')
            return render(request, 'app/signin.html')
    return render(request, 'app/signin.html')

def check_user(request):
    if request.method == "GET":
        un = request.GET["usern"]
        check = User.objects.filter(username=un)
        if len(check) == 1:
            return HttpResponse("Exists")
        else:
            return HttpResponse("Not Exists")


def signout(request):
    logout(request)
    return redirect('/')


def profile(request):
    if request.method == 'POST':
        name = request.POST['name']
        addr1 = request.POST['addr1']
        addr2 = request.POST['addr2']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        data = Profile(name=name,addr1=addr1,addr2=addr2,city=city,state=state,zipcode=zipcode)
        data.save()
        res = "Dear {} Your Profile is saved succesfully".format(name)
        return render(request,  'app/profile.html',{'status':res})
    return render(request,'app/profile.html')

def address(request):
    return render(request,  'app/address.html')

# def ticketbookingsystem(request):
#     if request.user.is_authenticated:
#         user = request.user
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             ticket = form.save(commit=False)
#             ticket.user = user
#             ticket.save()
#             return redirect('booking')
#         else:
#             form = TicketForm()
#     tickets = Ticket.objects.filter(user=user)
#     return render(request, 'app/booking.html', {'form':form,'tickets':tickets})
@login_required(login_url='signin') 
def ticketbookingsystem(request):
    user = request.user.id
    tickets = Ticket.objects.filter(user=user)
    if request.method == 'POST':
        nm = request.POST['full_name']
        sr = request.POST['source']
        dn = request.POST['destination']
        qn = request.POST['quantity']
        bd = request.POST['booking_date']
        tickets = Ticket.objects.filter(user=user)
        if sr != dn:
            tickets = Ticket.objects.create(user=request.user.id,full_name=nm,source=sr,destination=dn,quantity=qn,booking_date=bd)
            # tickets.save()
            return redirect('booking')
        else:
            messages.error(request,'Please Select Different Source and Destinations ')
            return redirect('booking')
    return render(request, 'app/booking.html',{'tickets':tickets})

     # tickets = Ticket.objects.create(user=request.user.id,full_name=nm,source=sr,destination=dn,quantity=qn,booking_date=bd)
        # tickets.save()
        # return redirect('booking')

        # tickets = Ticket.objects.filter(user=user)

def delete_ticket(request,pk):
    if request.method == 'POST':
        Ticket.objects.get(pk=pk).delete()
        return redirect('booking')

@login_required(login_url='signin') 
def confirm(request,pk):
        
        tickets = Ticket.objects.all()
        print(tickets)
        userid = pk
        form = TicketForm(request.POST)
        if form.is_valid():
            Ticket.objects.all(pk=pk)
            ticket = form.save(commit=False)
            ticket.save()
            return redirect('paypal')

        cart = Cart.objects.all()
        print(cart)
       
        return render(request, 'app/confirm.html', {'tickets':tickets, 'userid':userid, 'cart':cart})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        # date = request.POST['date']
        today = date.today()
        if len(phone) != 10:
            messages.error(request,"Please Enter Correct Phone NO")
            return render(request,'app/contact.html')
        data = Contact(name=name,email=email,phone=phone,message=message,date=today)
        data.save()
        res = "Dear {} Thanks for your feedback".format(name)
        return render(request,'app/contact.html',{'status':res})
    return render(request,'app/contact.html')

def view_profile(request):
    data = Register_table.objects.get(user__id = request.user.id)

    return render(request,'app/view_profile.html',{'data':data})

def edit_profile(request):

    data = Register_table.objects.get(user__id = request.user.id)
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        en = request.POST['email']
        cn = request.POST['contact_number']
        age = request.POST['age']
        cty = request.POST['city']
        occ = request.POST['occ']
        abt = request.POST['about']
        gen = request.POST['gender']

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = en
        usr.save()

        data.contact_number = cn
        data.age = age
        data.city = cty
        data.occupation = occ
        data.about = abt
        data.gender = gen
        data.save()
        # print(data.FILES)

        if 'profile_img' in request.FILES:
            img = request.FILES['profile_img']
            data.profile_pic = img
            data.save()
        messages.success(request,'Updated Successfully...!!!')
    return render(request,'app/edit_profile.html',{'data':data})

class change_password(View):    

    def get(self,request):
        return render(request,'app/change_password.html')

    def post(self,request):
        current_pas = request.POST['ppwd']
        new_pas = request.POST['npwd']
        user = User.objects.get(id=request.user.id)
        un = user.username
        pwd = new_pas
        check = user.check_password(current_pas)
        if check==True:
            user.set_password(new_pas)
            user.save()
            msz = "Password changed successfully"
            col = "alert-success"
            user = User.objects.get(username=un)
            login(request,user)
            return render(request,'app/change_password.html',{'msz':msz,'col':col})
        else:
            msz = "Incorrect Previous Password"
            col = "alert-danger"
            return render(request,'app/change_password.html',{'msz':msz,'col':col})

def add_to_list(request,offer_id):
    user = request.user
    offers_id = Offer.objects.get(pk=offer_id)
    Cart(user=user,offer=offers_id).save()
    return redirect('/cart')

def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        gst_tax = 40.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.offer.discount_price)
                amount += tempamount
                total_amount = amount + gst_tax
            return render(request ,'app/add-to-list.html',{'carts':cart,'total_amount':total_amount,'amount':amount,'gst_tax':gst_tax})
        else:
            return render(request,'app/emptycart.html')

def pluscart(request):
    if request.method == 'GET':
        offer_id = request.GET['offer_id']
        c = Cart.objects.get(Q(offer=offer_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        gst_tax = 40.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.offer.discount_price)
            amount += tempamount
            data = {
            'quantity': c.quantity,
            'amount':amount,
            'total_amount':amount + gst_tax
            }
        return JsonResponse(data)

def minuscart(request):
    if request.method == 'GET':
        offer_id = request.GET['offer_id']
        c = Cart.objects.get(Q(offer=offer_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        gst_tax = 40.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.offer.discount_price)
            amount += tempamount
            data = {
            'quantity': c.quantity,
            'amount':amount,
            'total_amount':amount + gst_tax
            }
        return JsonResponse(data)

def removecart(request):
    if request.method == 'GET':
        offer_id = request.GET['offer_id']
        Cart.objects.get(Q(offer=offer_id)&Q(user=request.user)).delete()
        return redirect("booking")


        # amount = 0.0
        # gst_tax = 40.0
        # cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        # for p in cart_product:
        #     tempamount = (p.quantity * p.offer.discount_price)
        #     amount += tempamount
        #     data = {
        #     'quantity': c.quantity,
        #     'amount':amount,
        #     'total_amount':amount + gst_tax
        #     }



    # @login_required
    # def customer(request):
    #     return render(request,'app/customer.html')

def place(request):
    
    return HttpResponse("Hello")

#@app.route("/payment",methods=('GET','POST'))
#class testpayment(View):
# def payment(request):
#     return render(request,'app/testpayment.html')

@login_required(login_url='signin') 
def paypal(request):
    return render(request , "app/paypal.html" )

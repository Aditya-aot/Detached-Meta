from contextvars import Context
import email
from itertools import product
from django.shortcuts import render , redirect
from .models import category_model , product_model ,cart_model
import razorpay
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def home_view(request) :

    category = category_model.objects.all()
    product = product_model.objects.all()
    top = product.filter(top_product=True)
    
    context = {
        'category' : category ,
        'top_product' : top[::-1] ,
    }
    return render(request, 'home/home.html',context)



@csrf_exempt
def detail_view(request,pk) :
    product = product_model.objects.all()
    product_info = product.filter(id=pk)
    price = product_info.values("price") 
    print(price[0])
    #  payment with Razorpay
    if request.method == 'POST' :
        client = razorpay.Client(auth=("rzp_test_MAGS2JFcBu5vr1", "ZWueXiUCqEgLzdgln0Q7OqgM"))

        DATA = {
            "amount": 1000 ,
            "currency": "INR",
            "receipt": "receipt#1",
            "notes": {
                "key1": "value3",
                "key2": "value2"
            }
        }
        payment = client.order.create(data=DATA)

        context = {
        'product' : product_info ,
        'top_product' : product ,
        'payment' : payment,
            }
        print("**********************************")
        print("**********************************")
        print(payment , payment['id'])
        print("**********************************")
        print("**********************************")
        # return render(request, 'home/detail_product.html',context)
        return redirect("/download_confirm/"+payment['id']+"/"+pk)

    #  payment with Razorpay
    else :
        print("**********************************")
        print("**********************************")
        # print(payment)
        print("**********************************")
        print("**********************************")
        context = {
            'product' : product_info ,
            'top_product' : product[::-1] ,
        }
        return render(request, 'home/detail_product.html',context)


def product_page_view(request) :
    product = product_model.objects.all()


    context = {
        'product' : product[::-1] ,
    }
    return render(request, 'home/product_page.html',context)


import ssl
import smtplib
from email.message import EmailMessage
@csrf_exempt
def download_confirm_view(request,order,pk) :
    product = product_model.objects.all()
    product_download = product.filter(id=pk)
    
    for i in product_download :
        link=i.link

    username_gmail = request.user.email
    print( username_gmail,'aditya sent>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    meassage = 'abcd '+ link
    
    
    
    email_sender = 'detachedmetastorage@gmail.com'
    email_password = 'jxrmqcpdgypqwyzv'
    email_receiver = username_gmail
    subject = 'Your 3d Model Link Enjoy'
    body = """
    Thank you for using our service , you product is in below Google link  
    """ + link 

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465 , context=context) as smtp :
        smtp.login('detachedmetastorage@gmail.com', 'jxrmqcpdgypqwyzv')
        smtp.sendmail('detachedmetastorage@gmail.com' , username_gmail , em.as_string())
   


    # server = smtplib.SMTP('smtp.gmail.com',587)
    # server.starttls()
    # server.login('detachedmetastorage@gmail.com', 'jxrmqcpdgypqwyzv')
    # server.sendmail('detachedmetastorage@gmail.com' , username_gmail , 'mail sent form me  aditya 3d model')
    print('sent>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    context = {
        'product' : product_download ,
    }
    return render(request, 'home/download_confirm.html',context)


def add_cart_view(request, pk) :
    print("----->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> out",pk)
    # if request.method == "POST" :
    # print("----->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>in",pk)
    user_cart = cart_model(user=request.user ,product_id=pk )
    user_cart.save()
    print("----->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>in",pk)
    return redirect("/cart")


def cart_view(request) :
    cart = cart_model.objects.all()
    cart_user = cart.filter(user=request.user)


    context = {
        'cart' : cart_user[::-1] ,
    }
    return render(request, 'home/cart.html',context)

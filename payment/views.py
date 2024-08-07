from decimal import Decimal
import stripe
from django.conf import settings 
from django.shortcuts import render,redirect,reverse,get_object_or_404
from orders.models import Order


# Create the stripe instance

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment_process(request):
    order_id=request.session.get('order_id',None)
    order=get_object_or_404(Order,id=order_id)

    if request.method == 'POST':
        success_url=request.build_absolute_uri(
            reverse('payment:payment_completed'))
        cancel_url=request.build_absolute_uri(
            reverse('payment:payment_canceled'))
        
        # stripe checkout session data
        session_data={
            'mode':'payment',
            'client_reference_id':order_id,
            'success_url':success_url,
            'cancel_url':cancel_url,
            'line_items':[]
        }

        #add order items to the stripe checkout session
        for item in order.items.all():
            session_data['line_items'].append({
                'price_data':{
                    'unit_amount':int(item.price*Decimal('100')),
                    'currency':'usd',
                    'product_data':{
                        'name':item.product.name,},
                    
                    },
                    'quantity':item.quantity,})
            
            #Stripe coupon
            if order.coupon:
                stripe_coupon=stripe.Coupon.create(
                    name=order.coupon.code,
                    percent_off=order.discount,
                    duration='once')
                session_data['discounts']=[{
                    'coupon':stripe_coupon.id,
                }]
        #create stripe checkout session
        session=stripe.checkout.Session.create(**session_data)

        #redirect to strie payment form
        return redirect(session.url,code=303)
    
    else:
        return render(request,'payment/process.html',locals())


def payment_completed(request):
    return render(request,'payment/completed.html')

def payment_cancelled(request):
    return render(request,'payment/canceled.html')

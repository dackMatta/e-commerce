from django.urls import reverse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import OrderItem,Order
from .forms import OrderCreateForm
from cart.cart import Cart


# Create your views here.

def order_create(request):
    cart=Cart(request)
    if request.method=='POST':
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            if cart.coupon:
                order.coupon=cart.coupon
                order.discount=cart.coupon.discount
            order.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            #clear cart
            cart.clear()

            #set the order in the session
            request.session['order_id'] = order.id

            #redirect for payment
            return redirect(reverse('payment:payment_process'))
        
    else:
        form = OrderCreateForm()

    return render(request, 'orders/create.html', 
                  {'cart': cart, 'form': form})

@staff_member_required
def admin_order_detail(request,order_id):
    order=get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/order/detail.html', {'order': order})





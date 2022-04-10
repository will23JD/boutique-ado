from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Kn1ZGFSFQJRU9hT7TYScwRXUsqRGaCVjuA3JkjB5W2k8FhIQLY7eXhTxVIBtmcmnbu9AVFq79HoVk5tir8my5wK00im8BPUYK',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

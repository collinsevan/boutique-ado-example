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
        'stripe_public_key': 'pk_test_51RP3EfQCwdMEhX8OQdxtAMSVvQSrDqtFMNCwUTNURlX0KTihLD7TJgsWQ3iAWXeyE2O7ETVkpMJPQmGqP5d1kHIl00mmnEdh5W', # noqa
        'client_secret': 'test client secret key',
    }

    return render(request, template, context)

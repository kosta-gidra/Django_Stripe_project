import stripe
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.conf import settings
from django.views import View
from .models import Order

stripe.api_key = settings.STRIPE_SEC_KEY


class ItemSuccessPageView(TemplateView):
    template_name = 'success.html'


class ItemCancelPageView(TemplateView):
    template_name = 'cancel.html'


class LandingPageView(TemplateView):
    template_name = 'landing.html'


class OrderPageView(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        order_id = self.kwargs['pk']
        order = Order.objects.get(id=order_id)
        context = super(OrderPageView, self).get_context_data(**kwargs)
        context.update({
            'order': order,
            'STRIPE_PUB_KEY': settings.STRIPE_PUB_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        order_id = self.kwargs['pk']
        order = Order.objects.get(id=order_id)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': order.get_price_cents(),
                        'product_data': {
                            'name': f'Order №{order.id}'
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.YOUR_DOMAIN + '/success/',
            cancel_url=settings.YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })

import stripe
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.conf import settings
from django.views import View
from .models import Item

stripe.api_key = settings.STRIPE_SEC_KEY


class ItemSuccessPageView(TemplateView):
    template_name = 'success.html'


class ItemCancelPageView(TemplateView):
    template_name = 'cancel.html'


class ItemPageView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        context = super(ItemPageView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUB_KEY': settings.STRIPE_PUB_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
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

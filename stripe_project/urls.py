from django.contrib import admin
from django.urls import path
from stripe_app.views import CreateCheckoutSessionView, ItemSuccessPageView, \
    ItemCancelPageView, OrderPageView, LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('success/', ItemSuccessPageView.as_view(), name='success-page'),
    path('cancel/', ItemCancelPageView.as_view(), name='cancel-page'),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('order/<pk>', OrderPageView.as_view(), name='order-page'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]

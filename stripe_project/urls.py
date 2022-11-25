from django.contrib import admin
from django.urls import path
from stripe_app.views import CreateCheckoutSessionView, ItemPageView, ItemSuccessPageView, ItemCancelPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('success/', ItemSuccessPageView.as_view(), name='success-page'),
    path('cancel/', ItemCancelPageView.as_view(), name='cancel-page'),
    path('item/<pk>', ItemPageView.as_view(), name='item-page'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]

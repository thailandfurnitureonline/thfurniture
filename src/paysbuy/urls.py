from django.conf.urls.defaults import patterns
from satchmo_store.shop.satchmo_settings import get_satchmo_setting

ssl = get_satchmo_setting('SSL', default_value=False)

urlpatterns = patterns('',
     (r'^$', 'src.paysbuy.views.pay_ship_info', {'SSL': ssl}, 'PAYSBUY_satchmo_checkout-step2'),
     (r'^confirm/$', 'src.paysbuy.views.confirm_info', {'SSL': ssl}, 'PAYSBUY_satchmo_checkout-step3'),
     (r'^success/$', 'src.paysbuy.views.success', {'SSL': ssl}, 'PAYSBUY_satchmo_checkout-success'),
     (r'^back/$', 'src.paysbuy.views.psb_back_resp', {'SSL': ssl}, 'PAYSBUY_satchmo_checkout-backend'),
     (r'^confirmorder/$', 'payment.views.confirm.confirm_free_order',
         {'SSL' : ssl, 'key' : 'PAYSBUY'}, 'PAYSBUY_satchmo_checkout_free-confirm')
)

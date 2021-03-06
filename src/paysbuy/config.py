from livesettings import *
from django.utils.translation import ugettext_lazy as _

# this is so that the translation utility will pick up the string
gettext = lambda s: s

PAYMENT_GROUP = ConfigurationGroup('PAYMENT_PAYSBUY',
    _('Paysbuy Payment Settings'),
    ordering=101)

config_register_list(

    StringValue(PAYMENT_GROUP,
        'CONNECTION',
        description=_("Live URL"),
        help_text=_("Url to submit live transactions."),
        default='https://www.paysbuy.com/paynow.aspx'),

    StringValue(PAYMENT_GROUP,
        'CONNECTION_TEST',
        description=_("Test URL"),
        help_text=("Url for test transactions"),
        default='http://demo.paysbuy.com/paynow.aspx'),

    BooleanValue(PAYMENT_GROUP,
        'LIVE',
        description=_("Accept real payments"),
        help_text=_("False if you want to submit to the test urls."),
        default=False),

    ModuleValue(PAYMENT_GROUP,
        'MODULE',
        description=_('Implementation module'),
        hidden=True,
        default = 'src.paysbuy'),

    StringValue(PAYMENT_GROUP,
        'KEY',
        description=_("Module key"),
        hidden=True,
        default = 'PAYSBUY'),

    StringValue(PAYMENT_GROUP,
        'LABEL',
        description=_('English name for this group on the checkout screens'),
        default = 'Paysbuy',
        dummy = _('Paysbuy'), # Force this to appear on po-files
        help_text = _('This will be passed to the translation utility')),

    StringValue(PAYMENT_GROUP,
        'URL_BASE',
        description=_('The url base used for constructing urlpatterns which will use this module'),
        default = r'^paysbuy/'),

    StringValue(PAYMENT_GROUP,
		#psb
        'PSB',
        description=_('Your Paysbuy.com merchant ID number'),
        default=""),
        
    StringValue(PAYMENT_GROUP,
		#psb
        'PSB_TEST',
        description=_('Test merchant ID number'),
        default="8303545188"),
        
    StringValue(PAYMENT_GROUP,
		#biz
        'BIZ',
        description=_('Your paysbuy.com merchant Username (email address)'),
        default=""),

    StringValue(PAYMENT_GROUP,
		#biz
        'BIZ_TEST',
        description=_('Paysbuy Test Email'),
        default="demo@paysbuy.com"),
        
    StringValue(PAYMENT_GROUP,
		#secureCode
        'SECURE_CODE',
        description=_('Your paysbuy.com secure code'),
        default=""),
        
    StringValue(PAYMENT_GROUP,
		#secureCode
        'SECURE_CODE_TEST',
        description=_('Test secure code'),
        default="15856093a8f80cbb5003001b42f0eeb7c"),
        
    StringValue(PAYMENT_GROUP,
		#currrencyCode
        'CURRENCY_CODE',
        description=_('Currency'),
        choices=(('764', _('Thai Bhat')),('036', _('Australian Dollar')),('826', _('Pound Sterling')),('978', _('Euro')),('344', _('Hong Kong Dollar')),('392', _('Yen (100)')),('554', _('New Zealand Dollar')),('702', _('Singapore Dollar')),('756', _('Swiss Franc')),('840', _('United States Dollar'))),
        default="764"),
        
    StringValue(PAYMENT_GROUP,
		#com
        'COMMISSION_CODE',
        description=_('A commission code for sending commision to another account'),
        help_text=("Contact PAYSBUY.com for more information"),
        default=""),
        
    StringValue(PAYMENT_GROUP,
		#method
        'PAY_METHOD',
        description=_('Default payment method'),
        choices=(('psb', _('Paysbuy Account')), ('c', _('Visa')), ('m', _('MasterCard')), ('j', _('JCB')), ('a', _('American Express')), ('p', _('PayPal')), ('cs', _('Counter Service')), ('ob', _('Online Banking'))),
        default="c"),
        
    StringValue(PAYMENT_GROUP,
		#language
        'LANGUAGE',
        description=_('Language in payment page'),
        choices=(('t', _('Thai')), ('e', _('English')), ('j', _('Japanese'))),
        default="e"),
        
    StringValue(PAYMENT_GROUP,
		#postURL
        'FRONT_URL',
        description=_('Rediect url upon payment completion'),
        default="http://your.domain/redirect/url/"),
        
    StringValue(PAYMENT_GROUP,
		#reqURL
        'BACK_URL',
        description=_('Backend response url'),
        default="http://your.domain/backend/url/"),
        
    BooleanValue(PAYMENT_GROUP,
		#opt_fix_redirect
        'OPT_FIX_REDIRECT',
        description=_('True to redirect without showing payment result'),
        help_text=("1 = not show payment result i.e. straight to redirect. Leave this blank to show payment result then redirect. This will redirect to RESP_FRONT_URL"),
        default=False),
        
    BooleanValue(PAYMENT_GROUP,
		#opt_fix_method
        'OPT_FIX_METHOD',
        description=_('True to only allow the default payment method. False to allow all'),
        default=False),
        
    BooleanValue(PAYMENT_GROUP,
        'CAPTURE',
        description=_('Capture Payment immediately?'),
        default=True,
        help_text=_('IMPORTANT: If false, a capture attempt will be made when the order is marked as shipped.')),

    BooleanValue(PAYMENT_GROUP,
        'EXTRA_LOGGING',
        description=_("Verbose logs"),
        help_text=_("Add extensive logs during post."),
        default=False),
)

PAYMENT_GROUP['TEMPLATE_OVERRIDES'] = {
    'shop/checkout/confirm.html' : 'confirm.html',
    'shop/checkout/success.html' : 'success.html',
    'shop/checkout/pay_ship.html' : 'pay_ship.html',
}

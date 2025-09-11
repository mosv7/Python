from .payment_common import IPayment
from .paypal_external import *

class PaypalPayment(IPayment):
    def __init__(self):
        super().__init__()
        self.paypal = PayPalOnlinePaymentAPI()
        self.card_info = PayPalCreditCard()
    
    def set_user_info(self, name, address):
        self.card_info.name = name
        self.card_info.address = address
    
    def set_card_info(self, id, expir_date, cvv):
        self.card_info.id = id
        self.card_info.expire_date = expir_date
        self.card_info.ccv = cvv
    
    def make_payment(self, money):
        self.paypal.card_info = self.card_info
        return self.paypal.pay_money(money)
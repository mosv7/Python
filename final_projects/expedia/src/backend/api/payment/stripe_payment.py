from .payment_common import IPayment
from .stripe_external import *

class StripPayment(IPayment):
    def __init__(self):
        super().__init__()
        self.card = StripeCardInfo()
        self.user = StripeUserInfo()

    def set_user_info(self, name, address):
        self.user.name = name
        self.user.address = address
    
    def set_card_info(self, id, expir_date):
        self.card.id = id
        self.card.expire_date = expir_date

    def make_payment(self, money):
        return StripePaymentAPI.withdraw_money(self.user, self.card, money)
    
    def cancel_payment(self, transaction_id):
        return StripePaymentAPI.cancel_money(transaction_id)


from abc import ABC, abstractmethod

class IPayment(ABC):
    @abstractmethod
    def set_user_info(self, name, address):
        pass

    @abstractmethod
    def set_card_info(self, id, expir_date, cvv):
        pass

    @abstractmethod
    def make_payment(self, money):
        pass

    @abstractmethod
    def cancel_payment(self, transaction_id):
        pass

class PaymentCard:
    def __init__(self, owner_name, card_number, expir_date, security_code, address):
        self.owner_name = owner_name
        self.card_number = card_number
        self.expir_date = expir_date
        self.security_code = security_code
        self.address = address
    
    def __repr__(self):
        return f'PaymentCard({self.owner_name}, {self.card_number}, {self.expir_date}, {self.security_code}, {self.address})'

class DepitCard(PaymentCard):
    def __init__(self, owner_name, card_number, expir_date, security_code, address):
        super().__init__(owner_name, card_number, expir_date, security_code, address)

class CreditCard(PaymentCard):
    def __init__(self, owner_name, card_number, expir_date, security_code, address):
        super().__init__(owner_name, card_number, expir_date, security_code, address)
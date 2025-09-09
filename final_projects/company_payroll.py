from abc import ABC, abstractmethod

class StaffMember:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Employee(StaffMember):
    def __init__(self, name, address, day_to_pay):
        super().__init__(name, address)
        self.day_to_pay = day_to_pay

class HourlyEmployee(Employee):
    def __init__(self, name, address, day_to_pay, total_working_hours, salary_per_hour):
        super().__init__(name, address, day_to_pay)
        self.total_working_hours = total_working_hours
        self.salary_per_hour = salary_per_hour
    
    @property
    def pay_amount(self):
        return self.total_working_hours * self.salary_per_hour

class SalariedEmployee(Employee):
    def __init__(self, name, address, day_to_pay, monthly_salary):
        super().__init__(name, address, day_to_pay)
        self.monthly_salary = monthly_salary
    
    @property
    def pay_amount(self):
        return self.monthly_salary

class CommissionSalariedEmployee(SalariedEmployee):
    def __init__(self, name, address, day_to_pay, monthly_salary, commission_rate, current_month_sales):
        super().__init__(name, address, day_to_pay, monthly_salary)
        self.commission_rate = commission_rate
        self.current_month_sales = current_month_sales
    @property
    def pay_amount(self):
        return super().pay_amount + (self.commission_rate * self.current_month_sales)

class Volunteer(StaffMember):
    def __init__(self, name, address, current_payment):
        super().__init__(name, address)
        self.current_payment = current_payment

    @property
    def pay_amount(self):
        return self.current_payment

class Item:
    def __init__(self, desc, price_per_one, quantity):
        self.desc = desc
        self.price_per_one = price_per_one
        self.quantity = quantity

    @property
    def price(self):
        return self.price_per_one * self.quantity

class Book(Item):
    def __init__(self, desc, price_per_one, quantity, author):
        super().__init__(desc, price_per_one, quantity)
        self.author = author
    

class Food(Item):
    def __init__(self, desc, price_per_one, quantity, expiration_date):
        super().__init__(desc, price_per_one, quantity)
        self.expiration_date = expiration_date

class ValidationRule(ABC):
    @abstractmethod
    def is_valid_rule(self, invoice):
        pass

class TaxesValidationRule(ValidationRule):
    def is_valid_rule(self, invoice):
        print('validating taxesvalidationrule')
        return True

class SuppliersDealsValidationRule(ValidationRule):
    def is_valid_rule(self, invoice):
        print('validating suppliersdealsvalidationrule')
        return True

class InvoiceValidator:
    def __init__(self, rules):
        self.rules = rules
    
    def validate(self, invoice: ValidationRule):
        if not self.rules:
            raise ValueError("No validation rules provided")
        
        for rule in self.rules:
            if not rule.is_valid_rule(invoice):
                return False
        return True

class MandatoryInvoiceValidator(InvoiceValidator):
    @staticmethod
    def get_instance():
        rules = [TaxesValidationRule()]
        return MandatoryInvoiceValidator(rules)


class CompleteInvoiceValidator(InvoiceValidator):
    @staticmethod
    def get_instance():
        rules = [TaxesValidationRule(), SuppliersDealsValidationRule()]
        return CompleteInvoiceValidator(rules)

class ValidationError(BaseException):
    pass

class Invoice:
    def __init__(self, invoice_id, validator: InvoiceValidator):
        self.invoice_id = invoice_id
        self.validator = validator
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    @property
    def pay_amount(self):
        if not self.validator.validate(self):
            raise ValidationError('One of the invoices are invalid')
        return sum([item.price for item in self.items])

class Payroll:
    def __init__(self):
        self.payabels = []
    
    def add_payable(self, payable):
        self.payabels.append(payable)
    
    @property
    def pay_amount(self):
        return sum(payable.pay_amount for payable in self.payabels)

class Company:
    def __init__(self):
        self.payroll = Payroll()
    
    def fill_data(self, is_mandatory_validator=True):
        self.payroll.add_payable(Volunteer('Most', 'AddressV', 700))
        self.payroll.add_payable(HourlyEmployee('Belal', 'AddressH', 1, 10, 3))
        self.payroll.add_payable(SalariedEmployee('Ziad', 'AddressS1', 2, 3000))
        self.payroll.add_payable(SalariedEmployee('Ashraf', 'AddressS1', 2, 3000))
        self.payroll.add_payable(CommissionSalariedEmployee('Safa', 'AddressC1', 6, 2500, 0.001, 5000))
        self.payroll.add_payable(CommissionSalariedEmployee('ahmed', 'AddressC2', 6, 2500, 0.001, 5000))

        if is_mandatory_validator:
            validator = MandatoryInvoiceValidator.get_instance()
        else:
            validator = CompleteInvoiceValidator.get_instance()
        invoice = Invoice(1234, validator)
        invoice.add_item(Book('book1', 10, 7, ''))
        invoice.add_item(Food('food1', 5, 6, ''))
        self.payroll.add_payable(invoice)

if __name__ == "__main__":
    company = Company()
    company.fill_data(False)
    print(f'Total Payroll: {company.payroll.pay_amount}')
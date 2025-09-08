from .employee import Employee
from ..common.utilites import input_valid_int

class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('\nEnter employee data:')
        name = input('Enter the name: ')
        age = input_valid_int('Enter the age: ')
        salary = input_valid_int('Enter the salary: ')

        self.employees.append(Employee(name, age, salary))
    
    def list_employees(self):
        if len(self.employees) == 0:
            print('\nNo employees at the moment!')
            return
        
        print('\n**Employees list**')
        for emp in self.employees:
            print(emp)

    def Delete_by_age_range(self, age_from, age_to):
        for idx in range(len(self.employees)-1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print(f'\tDeleting', emp.name)
                self.employees.pop(idx)
    
    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)

        if emp is None:
            print('Error: No employee with such a name')
        else:
            emp.salary = salary
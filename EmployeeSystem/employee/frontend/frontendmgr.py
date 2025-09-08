from ..backend.employeesmgr import EmployeesManager
from ..common.utilites import input_valid_int

class FrontendManager:
    def __init__(self):
        self.employees_manager = EmployeesManager()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = F'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))


    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employees_manager.add_employee()
            elif choice == 2:
                self.employees_manager.list_employees()
            elif choice == 3:
                age_from = input_valid_int('Enter age from: ')
                age_to = input_valid_int('Enter age to: ')

                self.employees_manager.Delete_by_age_range(age_from, age_to)
            elif choice == 4:
                name = input('Enter name: ')
                salary = input_valid_int('Enter new salary: ')
                self.employees_manager.update_salary_by_name(name, salary)
            else:
                exit()
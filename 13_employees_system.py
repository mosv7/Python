# class Employee:
#     employees = []

#     def add_new_emp(name, age, salary):
#         Employee.employees.append((name, age, salary))

#     def list_all_emps():
#         return Employee.employees
    
#     def delete_by_age_range(From, to):
#         deleted = []

#         for idx in range(len(Employee.employees) - 1, -1, -1):
#             if From <= Employee.employees[idx][1] <= to:
#                 emp = Employee.employees.pop(idx)
#                 deleted.append(emp[0])

#         return deleted

#     def update_salary(emp_name, new_salary):
#         for idx, (name, age, _) in enumerate(Employee.employees):
#             if name == emp_name:
#                 Employee.employees[idx] = (name, age, new_salary)


# class clsmainscreen:
#     def draw_main_screen(self):
#         print('''
# Program Options:
# 1) Add a new employee
# 2) List all employees
# 3) Delete by age range
# 4) Update salary given a name
# 5) End the program
# ''')
    
#     def input_validation(self):
#         num = int(input('Enter your choice (from 1 to 5): '))

#         while(not(0 < num < 6)):
#             print('Invalid range. Try again!')
#             num = int(input('Enter your choice (from 1 to 5): '))
        
#         return num

#     def add_new_emp_screen(self):
#         print('\nEnter employee data: ')
#         name = input('Enter the name: ')
#         age = int(input('Enter the age: '))
#         salary = int(input('Enter the salary: '))
#         Employee.add_new_emp(name, age, salary)

#     def list_emps_screen(self):
#         if len(Employee.list_all_emps()) == 0:
#             print('\nThere is no Employees yet!')
#         else:
#             print('\n**Employees list**')
#             for (name, age, salary) in Employee.list_all_emps():
#                 print(f'Employee: {name} has age {age} and salary {salary}')

#     def delete_emps_by_range_screen(self):
#         From = int(input('Enter age from: '))
#         to = int(input('Enter age to: '))
#         deleted = Employee.delete_by_age_range(From, to)
#         for name in deleted:
#             print(f'\tDeleting {name}')

#     def Update_salary_screen(self):
#         name = input('Enter name: ')
#         salary = int(input('Enter new salary: '))
#         Employee.update_salary(name, salary)

#     def mainpulat_screen(self, choice):
#         emp = Employee()
#         if choice == 1:
#             # print('Add a new employee screen will be here')
#             self.add_new_emp_screen()
#         elif choice == 2:
#             #print('List all employees screen will be here')
#             self.list_emps_screen()
#         elif choice == 3:
#             #print('Delete by age range screen will be here')
#             self.delete_emps_by_range_screen()
#         elif choice == 4:
#             #print('Update salary given a name will be here')
#             self.Update_salary_screen()
#         else:
#             exit()

#     def main_menu(self):
#         while True:
#             self.draw_main_screen()
#             choice = self.input_validation()
#             self.mainpulat_screen(choice)

# main_menu = clsmainscreen()
# main_menu.main_menu()

def input_valid_int(msg, start = 0, end = None):
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid range. Try again!')
        
        elif end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
            else:
                return int(inp)
        
        else:
            return int(inp)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f'Employee: {self.name} has age {self.age} and salary {self.salary}'
    
    def __repr__(self):
        return f'Employee(name={self.name}, age={self.age}, salary={self.salary})'

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


Frontend = FrontendManager()
Frontend.run()
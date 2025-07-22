class Employee:
    employees = []

    def add_new_emp(name, age, salary):
        Employee.employees.append((name, age, salary))

    def list_all_emps():
        return Employee.employees
    
    def delete_by_age_range(From, to):
        deleted = []

        for idx in range(len(Employee.employees) - 1, -1, -1):
            if From <= Employee.employees[idx][1] <= to:
                emp = Employee.employees.pop(idx)
                deleted.append(emp[0])

        return deleted

    def update_salary(emp_name, new_salary):
        for idx, (name, age, _) in enumerate(Employee.employees):
            if name == emp_name:
                Employee.employees[idx] = (name, age, new_salary)


class clsmainscreen:
    def draw_main_screen(self):
        print('''
Program Options:
1) Add a new employee
2) List all employees
3) Delete by age range
4) Update salary given a name
5) End the program
''')
    
    def input_validation(self):
        num = int(input('Enter your choice (from 1 to 5): '))

        while(not(0 < num < 6)):
            print('Invalid range. Try again!')
            num = int(input('Enter your choice (from 1 to 5): '))
        
        return num

    def add_new_emp_screen(self):
        print('\nEnter employee data: ')
        name = input('Enter the name: ')
        age = int(input('Enter the age: '))
        salary = int(input('Enter the salary: '))
        Employee.add_new_emp(name, age, salary)

    def list_emps_screen(self):
        if len(Employee.list_all_emps()) == 0:
            print('\nThere is no Employees yet!')
        else:
            print('\n**Employees list**')
            for (name, age, salary) in Employee.list_all_emps():
                print(f'Employee: {name} has age {age} and salary {salary}')

    def delete_emps_by_range_screen(self):
        From = int(input('Enter age from: '))
        to = int(input('Enter age to: '))
        deleted = Employee.delete_by_age_range(From, to)
        for name in deleted:
            print(f'\tDeleting {name}')

    def Update_salary_screen(self):
        name = input('Enter name: ')
        salary = int(input('Enter new salary: '))
        Employee.update_salary(name, salary)

    def mainpulat_screen(self, choice):
        emp = Employee()
        if choice == 1:
            # print('Add a new employee screen will be here')
            self.add_new_emp_screen()
        elif choice == 2:
            #print('List all employees screen will be here')
            self.list_emps_screen()
        elif choice == 3:
            #print('Delete by age range screen will be here')
            self.delete_emps_by_range_screen()
        elif choice == 4:
            #print('Update salary given a name will be here')
            self.Update_salary_screen()
        else:
            exit()

    def main_menu(self):
        while True:
            self.draw_main_screen()
            choice = self.input_validation()
            self.mainpulat_screen(choice)

main_menu = clsmainscreen()
main_menu.main_menu()
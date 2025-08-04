class patient:
    def __init__(self, name, specialization, status):
        self.name = name
        self.specialization = specialization
        self.status = status  # 1: Normal, 2: Urgent, 3: Super Urgent

    def __str__(self):
        if self.status == 1:
            status_str = 'Normal'
        elif self.status == 2:
            status_str = 'Urgent'
        elif self.status == 3:
            status_str = 'Super Urgent'
        return f'Patient: {self.name} is {status_str}'
    
    def __repr__(self):
        return f'Patient(name={self.name}, specialization={self.specialization}, status={self.status})'

class Backend:
    def __init__(self):
        self.specializations = [None] * 20

    def _check_fullqueue(self, specialization):
        if self.specializations[specialization - 1] is None:
            return False
        sum = 0
        for lst in self.specializations[specialization - 1].values():
            sum += len(lst)
        return sum >= 10

    def _get_patient_count(self, specialization):
        sum = 0
        for lst in self.specializations[specialization - 1].values():
            sum += len(lst)
        return sum

    def _add_patient(self, name, specialization, status):
        if self._check_fullqueue(specialization):
            print('Queue is full for this specialization.')
            return
        elif self.specializations[specialization - 1] is None:
            self.specializations[specialization - 1] = {}
        self.specializations[specialization - 1].setdefault(status, []).append(patient(name, specialization, status))

    def _get_all_patients(self):
        # Return only dicts that have at least one non-empty patient list
        result = []
        for d in self.specializations:
            if d is not None and isinstance(d, dict) and any(isinstance(lst, list) and lst for lst in d.values()):
                result.append(d)
        return result

    def _get_next_patient(self, specialization):
        if self.specializations[specialization - 1] is None or self.specializations[specialization - 1] == {}:
            return None
        for status in [3, 2, 1]:
            if status in self.specializations[specialization - 1]:
                return self.specializations[specialization - 1][status].pop(0)
        return None
    
    def _get_patient_by_name(self, specialization, name):
        if self.specializations[specialization - 1] is None or self.specializations[specialization - 1] == {}:
            return None
        for status in [3, 2, 1]:
            if status in self.specializations[specialization - 1]:
                for patient in self.specializations[specialization - 1][status]:
                    if patient.name == name:
                        return patient
        return None

    def _remove_patient(self, specialization, name):
        patient = self._get_patient_by_name(specialization, name)

        if patient:
            for status in [3, 2, 1]:
                if status in self.specializations[specialization - 1]:
                    if patient in self.specializations[specialization - 1][status]:
                        self.specializations[specialization - 1][status].remove(patient)
                        print(f'\nPatient {name} has been removed from the queue.\n')
                        return True
        else:
            print(f'\nPatient {name} not found in specialization {specialization}.\n')
            return False

class Frontend:
    def __init__(self):
        self.backend = Backend()

    def _draw_menu(self):
        print('program options: ')
        print('1. Add patient')
        print('2. View patients')
        print('3. Get next patient')
        print('4. remove leaving patient')
        print('5. Exit')

    def _input_validation(self, msg, from_, to):
        value = int(input(msg))
        while not (from_ <= value <= to):
            print(f'Please enter a number between {from_} and {to}')
            value = int(input(msg))
        return value

    def _add_patient_screen(self):
        name = input('Enter patient name: ')
        specialization = self._input_validation('Enter patient specialization: ', 1, 20)
        status = self._input_validation('Enter patient status: ', 1, 3)
        # add patient to backend
        self.backend._add_patient(name, specialization, status)

    def str_status(self, status):
        if status == 1:
            return 'Normal'
        elif status == 2:
            return 'Urgent'
        else:
            return 'Super Urgent'

    def _view_patients_screen(self):
        if not self.backend.specializations:
                print('\nNo patients available.\n')
        else:
            # Display all patients
            for dict in self.backend._get_all_patients():
                patient_count = self.backend._get_patient_count(dict[1][0].specialization)
                print(f'\nSpecialization {dict[1][0].specialization}, There are {patient_count} patients:')

                for patients in reversed(dict.values()):
                    for patient in patients:
                            print(patient)
            print('\n')

    def _get_next_patient_screen(self):
        specialization = self._input_validation('Enter specialization to get next patient: ', 1, 20)
        if patient := self.backend._get_next_patient(specialization):
            print(f'\n{patient.name}, please proceed to the doctor.\n')
        else:
            print('\nNo patients available in this specialization.\n')

    def _remove_leaving_patient_screen(self):
        specialization = self._input_validation('Enter specialization to remove leaving patient: ', 1, 20)
        name = input('Enter patient name to remove: ')
        self.backend._remove_patient(specialization, name)

    def _manipulate_choice(self, choice):
        if choice == 1:
            self._add_patient_screen()
        elif choice == 2:
            self._view_patients_screen()
        elif choice == 3:
            self._get_next_patient_screen()
        elif choice == 4:
            self._remove_leaving_patient_screen()
        else:
            print('\nExiting the program.\n')
            exit()

    def dummydata(self):
        # Specialization 0: Cardiology
        self.backend.specializations[0] = {
            # Key = 1 → Normal
            1: [
                patient('John Doe', 1, 1),
                patient('Alice Johnson', 1, 1),
                patient('Michael Lee', 1, 1)
            ],
            # Key = 2 → Urgent
            2: [
                patient('Jane Smith', 1, 2),
                patient('David Kim', 1, 2)
            ],
            # Key = 3 → Super Urgent
            3: [
                patient('Bob Brown', 1, 3),
                patient('Elena Ruiz', 1, 3)
            ]
        }

        # Specialization 1: Pediatrics
        self.backend.specializations[1] = {
            1: [  # Normal
                patient('Charlie White', 2, 1),
                patient('Lucas Garcia', 2, 1),
                patient('Mia Thompson', 2, 1),
                patient('Isabella Young', 2, 1),
            ],
            2: [  # Urgent
                patient('Diana Green', 2, 2),
                patient('Emma Robinson', 2, 2),
                patient('Oliver Martinez', 2, 2)
            ],
            3: [  # Super Urgent
                patient('Noah Clark', 2, 3),
                patient('Ava Rodriguez', 2, 3),
                patient('Sophia Chen', 2, 3)
            ]
        }

        # Specialization 2: Orthopedics
        self.backend.specializations[2] = {
            1: [
                patient('James Wilson', 3, 1),
                patient('Grace Hill', 3, 1)
            ],
            2: [
                patient('Henry Allen', 3, 2),
                patient('Zoe Baker', 3, 2)
            ],
            3: [
                patient('Liam Scott', 3, 3)
            ]
        }

        # Specialization 3: Neurology
        self.backend.specializations[3] = {
            1: [
                patient('Emily Nelson', 4, 1),
                patient('Daniel Hall', 4, 1),
                patient('Connor Cook', 4, 1)
            ],
            2: [
                patient('Sarah King', 4, 2),
                patient('Matthew Wright', 4, 2)
            ],
            3: [
                patient('Samantha Lopez', 4, 3),
                patient('Ethan Perez', 4, 3)
            ]
        }

        # Specialization 4: Dermatology
        self.backend.specializations[4] = {
            1: [
                patient('Ryan Carter', 5, 1),
                patient('Natalie Ramirez', 5, 1),
                patient('Oscar Sanchez', 5, 1)
            ],
            2: [
                patient('Abigail Reed', 5, 2)
            ],
            3: [
                patient('Lily Morgan', 5, 3),
                patient('Benjamin Reed', 5, 3)
            ]
        }
        # Specialization 16: General Medicine
        self.backend.specializations[16] = {
            1: [
                patient('Alice Smith', 17, 1),
                patient('Bob Johnson', 17, 1)
            ],
            2: [
                patient('Charlie Brown', 17, 2)
            ],
            3: [
                patient('Diana White', 17, 3)
            ]
        }

        self.backend._add_patient('ahmed', 20, 1)

    def start_menu(self):
        self.dummydata()
        while True:
            self._draw_menu()
            choice = self._input_validation('Please enter your choice: ', 1, 5)
            self._manipulate_choice(choice)


# frontend = Frontend()
# frontend.start_menu()

# the doctor code
def input_valid_int(msg, start = 0, end = None):
    # keep iterating till the given input is valid
    # hidden assumption: both start and end either value or none. That is bad
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
                # another way is to check if int(inp) in range(start, end+1)
            else:
                return int(inp)
        else:
            return int(inp)


class Patient:
    def __init__(self, name, status):
        self.name, self.status = name, status

    def __str__(self):
        status = ['Normal', 'Urgent', 'Super Urgent'][self.status]
        return f'Patient: {self.name} is {status}'

    def __repr__(self):
        return F'Patient(name="{self.name}", status={self.status})'

    def __lt__(self, other):    # see: def add_patient_smart
        return self.status > other.status   # given 2 patients: which one comes first? one with bigger status


# Observe. In this manager, there is only logic
# All interaction with user (read/write) are at the front end
class HospitalManger:
    def __init__(self, specializations_cnt):
        self.specializations = [[] for s in range(specializations_cnt)]
        self.MAX_QUEUE = 10
        self.NORMAL = 0
        self.URGENT = 1
        self.SUPER_URGENT = 2

    def can_add_more_patients(self, specialization):
        return len(self.specializations[specialization]) < self.MAX_QUEUE

    def add_patient_smart(self, specialization, name, status): # ignore for now or google
        spec = self.specializations[specialization]
        spec.append(Patient(name, status))  # Add at end
        spec.sort() # in-place sort based on large status first. it preserves the old order!
        # as python don't know how to compare objects (which comes first), you need to add __lt__

    def add_patient(self, specialization, name, status):
        spec = self.specializations[specialization]
        pat = Patient(name, status)

        if status == 0 or len(spec) == 0:           # Add normal
            spec.append(pat)      # Add at end
        elif status == 1:   # Add urgent
            # Add before the normal patients, but after current urgents / super-urgents
            if spec[-1].status != self.NORMAL:      # if no normals, then it should be added after the end
                spec.append(pat)
            else:   # Find the first normal and add before it
                for idx, patient in enumerate(spec):
                    if patient.status == self.NORMAL:
                        spec.insert(idx, pat)
                        break
        else:
            # Add before the normal or urgent patients, but after current super-urgents
            if spec[-1].status == self.SUPER_URGENT:      # if all are super urgent, just add at the end
                spec.append(pat)
            else:   # Find the first normal/urgent and add before it
                for idx, patient in enumerate(spec):
                    if patient.status == self.NORMAL or patient.status == self.URGENT:
                        spec.insert(idx, pat)
                        break

    def get_printable_patients_info(self):
        results = []    # send back results to front end to print on its way
        for idx, specialization in enumerate(self.specializations):
            if not specialization:
                continue
            cur_patients = []
            for patient in specialization:
                cur_patients.append(str(patient))
            results.append((idx, cur_patients))
        return results

    def get_next_patients(self, specialization):
        if len(self.specializations[specialization]) == 0:
            return None
        return self.specializations[specialization].pop(0)

    def remove_patient(self, specialization, name):
        spec = self.specializations[specialization]
        for idx, patient in enumerate(spec):
            if patient.name == name:
                del spec[idx]
                return True
        return False


class FrontendManager:
    def __init__(self, specializations_cnt = 20):
        self.specializations_cnt = specializations_cnt
        self.hospital_manger = HospitalManger(self.specializations_cnt)
        self.add_dummy_data()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            'Add new patient',
            'Print all patients',
            'Get next patient',
            'Remove a leaving patient',
            'End the program'
        ]
        # let's add the order 1 2 3 4...
        messages = [f'{idx+1}) {msg}' for idx, msg in enumerate(messages)]
        print('\n'.join(messages))
        msg = f'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    def add_dummy_data(self):
        for i in range(10):
            self.hospital_manger.add_patient(2, 'Dummy' + str(i), i % 3)
        for i in range(4):
            self.hospital_manger.add_patient(5, 'AnotherDummy' + str(i), 0)
        for i in range(5):
            self.hospital_manger.add_patient(8, 'ThirdDummy' + str(i), 1)
        for i in range(3):
            self.hospital_manger.add_patient(12, 'ForthDummy' + str(i), 2)
        for i in range(3):
            self.hospital_manger.add_patient(13, 'FifthDummy' + str(i), 1)
            self.hospital_manger.add_patient(13, 'FifthDummy' + str(i+5), 2)

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                specialization = input_valid_int('Enter specialization: ', 1, self.specializations_cnt) - 1

                if self.hospital_manger.can_add_more_patients(specialization):
                    name = input('Enter patient name: ')
                    status = input_valid_int('Enter status (0 normal / 1 urgent / 2 super urgent): ', 0, 2)
                    self.hospital_manger.add_patient(specialization, name, status)
                else:
                    print("Sorry we can't add more patients for this specialization at the moment.")
            elif choice == 2:
                results = self.hospital_manger.get_printable_patients_info()
                if not results:
                    print('No patients at the moment')
                else:
                    for idx, patients_info in results:
                        print(f'Specialization {idx+1}: There are {len(patients_info)} patients.')
                        print("\n".join(patients_info) + '\n')
            elif choice == 3:
                specialization = input_valid_int('Enter specialization: ', 1, self.specializations_cnt) - 1
                patient = self.hospital_manger.get_next_patients(specialization)

                if patient is None:
                    print('No patients at the moment. Have rest, Dr')
                else:
                    print(f'{patient.name}, Please go with the Dr')
            elif choice == 4:
                specialization = input_valid_int('Enter specialization: ', 1, self.specializations_cnt) - 1
                name = input('Enter patient name: ')
                if not self.hospital_manger.remove_patient(specialization, name):
                    print('No patient with such a name in this specialization!')
            else:
                break


if __name__ == '__main__':
    app = FrontendManager()
    app.run()
from ..backend.users_mgr import UsersManager
from .utils import get_menu_choice

class SiteAccessManager:
    def __init__(self):
        self.users_manager = UsersManager()
    
    def print_menu(self):
        return get_menu_choice('System Access:', ['Login', 'Sign up [NA]'])
    
    def get_accessed_user(self):
        funcs = [self.login, self.signup]

        while True:
            choice = self.print_menu()
            user = funcs[choice - 1]()

            if user is not None:
                return user
            else:
                print('Please try again')

    def login(self):
        username = input('Enter username: ')
        password = input('Enter password: ')

        user = self.users_manager.get_user(username, password)
        if user is None:
            print('Invalid username or password')

        return user

    def signup(self):
        raise NotImplementedError('Signup is not implemented yet')
class User:
    '''
    class that generates new instance of user
    '''
    user_list = []

    def __init__(self, login_name, password):
        '''
        this method ddefines properties for our user object
        '''
        self.login_name = login_name
        self.password = password

    def save_user(self):
        '''
        method to save a new users
        '''

        User.user_list.append(self)

    @classmethod
    def user_login(cls, login):
        '''
        method to check login credentials
        '''
        for User in cls.user_list:
            if User.login_name == login:
                return User

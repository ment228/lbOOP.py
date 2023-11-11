'''print(type(-5))
print(type('python'))
class User:
    user_name = 'Admin'
    password = 'qwerty'
user_1 = User() #создание объекта класса
print(user_1.__dict__)
print(User.__dict__)
print(user_1.user_name)
user_1.name = 'Tom'
user_1.user_name = 'Tom'
print(user_1.__dict__)'''
class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def print_info(self):
        print(f'логин: {self.name}\nПароль: {self.password}')
user_1 = User('Tom')
user_1.print_info()
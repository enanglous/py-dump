# OOP

# class PlayerCharacter:
#     # class object attribute
#     _membership = False
#     _name = 'Anonymous'
#     _age = 0

#     # constructor method - gets called every time we create an instance of the class
#     def __init__(self, age=0, **kwargs):  # kwargs - keyword arguments
#         if kwargs['membership']:
#             self._membership = kwargs['membership']
#         if age >= 18:
#             self._name = kwargs['name']
#             self._age = age
#     # instance method - gets called every time we create an instance of the class

#     def run(self):
#         return self

#     def speak(self):
#         print(f'My name is {self._name}, and I am {self._age} years old.')

#     @classmethod  # decorator
#     def define(cls):
#         return cls(18, name='Teddy', membership=True)

#     @staticmethod  # decorator
#     def adding_things(num1, num2):
#         return num1 + num2


# def fun(**kwargs):
#     self.name = kwargs['name']


# fun(name='Teddy', age=18, membership=True)
# class method creates an instance of the class with name teddy and age 18
# print(PlayerCharacter.define())
# static method does not create an instance of the class
# print(PlayerCharacter.adding_things(2, 3))

# playing with self
# player1 = PlayerCharacter(18, name='Teddy', membership=True)
# print(player1)
# print(player1.run)
# print(player1.run().run)

# never do this (VERY BAD PRACTICE)
# player1 = PlayerCharacter(18, name='Teddy', membership=True)
# player1._name = 'John'
# print(player1._name)


# Path: main.py
# Inheritance
# class User:
#     _type = None
#     _loggedIn = False

#     def sign_in(self):
#         self._loggedIn = True
#         print('Logged in')


# class Wizard(User):  # Wizard class inherits from User class
#     _name = 'Anonymous'
#     _power = 0

#     def __init__(self, name, power):
#         self._name = name
#         self._power = power
#         User._type = 'Wizard'
#         User.sign_in()

#     def attack(self):
#         print(f'Attacking with power of {self._power}')


# class Archer(User):
#     _name = 'Anonymous'
#     _num_arrows = 0

#     def __init__(self, name, num_arrows):
#         self._name = name
#         self._num_arrows = num_arrows
#         User._type = 'Archer'

#     def attack(self):
#         print(f'Attacking with arrows: arrows left - {self._num_arrows}')


# wizard1 = Wizard('Merlin', 50)

# wizard1.sign_in()


# Path: main.py
# Polymorphism
# class User:
#     _type = None
#     _loggedIn = False
#     _email = ''

#     def __init__(self, email):
#         self._email = email

#     def sign_in(self):
#         self._loggedIn = True
#         print('Logged in')

#     def attack(self):
#         print('Do nothing')


# class Wizard(User):  # Wizard class inherits from User class
#     _name = 'Anonymous'
#     _power = 0

#     def __init__(self, name, power, email):
#         super().__init__(email)  # super() - calls the parent class
#         self._name = name
#         self._power = power
#         User._type = 'Wizard'
#         User.sign_in(self)

#     def attack(self):
#         User.attack(self)
#         print(f'Attacking with power of {self._power}')

#     def run(self):
#         print('Run really fast')


# class Archer(User):
#     _name = 'Anonymous'
#     _num_arrows = 0

#     def __init__(self, name, num_arrows):
#         self._name = name
#         self._num_arrows = num_arrows
#         User._type = 'Archer'

#     def attack(self):
#         print(f'Attacking with arrows: arrows left - {self._num_arrows}')

#     def run(self):
#         print('Run really fast')


# wizard1 = Wizard('Merlin', 50, 'wot@gmail.com')
# archer1 = Archer('Robin', 100)
# wizard1.attack()
# archer1.attack()
# wizard1.run()
# archer1.run()
# print(isinstance(wizard1, Wizard))
# print(isinstance(wizard1, User))
# print(isinstance(wizard1, object))
# print(isinstance(wizard1, Archer))
# print(isinstance(wizard1, int))
# print(isinstance(wizard1, str))


# Dunder methods

class Toy:
    def __init__(self, color, age):
        self._color = color
        self._age = age
        self._my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self._color}'

    def __len__(self):
        return 5

    def __call__(self):
        return 'yes?'

    def __getitem__(self, i):
        return self._my_dict[i]


action_figure = Toy('red', 0)

# print(action_figure.__str__())  # same as print(str(action_figure))
# print(str(action_figure))
# print(len(action_figure))
# print(action_figure.__len__())  # same as print(len(action_figure))
# print(action_figure())
# print(action_figure.__call__())  # same as print(action_figure())

print(action_figure['name'])
print(action_figure['has_pets'])

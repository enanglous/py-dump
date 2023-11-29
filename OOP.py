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
#     _loggedIn = False   # private variables because they start with _

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

# class Toy:
#     def __init__(self, color, age):
#         self._color = color
#         self._age = age
#         self._my_dict = {
#             'name': 'Yoyo',
#             'has_pets': False
#         }

#     def __str__(self):
#         return f'{self._color}'

#     def __len__(self):
#         return 5

#     def __call__(self):
#         return 'yes?'

#     def __getitem__(self, i):
#         return self._my_dict[i]


# action_figure = Toy('red', 0)

# print(action_figure.__str__())  # same as print(str(action_figure))
# print(str(action_figure))
# print(len(action_figure))
# print(action_figure.__len__())  # same as print(len(action_figure))
# print(action_figure())
# print(action_figure.__call__())  # same as print(action_figure())

# print(action_figure['name'])
# print(action_figure['has_pets'])


# Path: main.py
# Exercise dunder methods

# create a superlist class that behaves like a list but has a dunder method len that always returns 1000
# class SuperList(list):
#     def __len__(self):
#         return 1000


# super_list1 = SuperList()

# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])
# print(issubclass(SuperList, list))
# print(issubclass(list, object))
# print(issubclass(SuperList, object))


# Path: main.py
# Multiple inheritance
# class User:
#     _type = None
#     _loggedIn = False   # private variables because they start with _

#     def sign_in(self):
#         self._loggedIn = True
#         print('Logged in')

#     def attack(self):
#         print('Do nothing')


# class Wizard(User):  # Wizard class inherits from User class
#     _name = 'Anonymous'
#     _power = 0

#     def __init__(self, name, power):
#         # super().__init__(email)  # super() - calls the parent class
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

#     def check_arrows(self):
#         print(f'{self._num_arrows} remaining')

#     def run(self):
#         print('Run really fast')


# class HybridBorg(Wizard, Archer):  # inherits from Wizard AND Archer
#     def __init__(self, name, power, num_arrows):
#         Archer.__init__(self, name, num_arrows)
#         Wizard.__init__(self, name, power)


# hb1 = HybridBorg('Borgie', 50, 100)
# print(hb1.attack())  # which method will be called here?
# # I still have no idea

# print(hb1.check_arrows())
# print(hb1.sign_in())
# print(hb1.run())


# Path: main.py
# Method Resolution Order (MRO)
# print(HybridBorg.__mro__)
# (<class '__main__.HybridBorg'>, <class '__main__.Wizard'>, <class '__main__.Archer'>, <class '__main__.User'>, <class 'object'>)
# the order in which Python will look for methods and attributes
# in this case, it will look for the method in HybridBorg, then in Wizard, then in Archer, then in User, then in object
# the order is determined by the order of the classes in the class definition
# if we switch Wizard and Archer, the order will change

#       A # A is the parent class
#      / \
#     /   \
#    B     C  # B and C inherit from A
#     \   /
#      \ /
#       D # D inherits from B and C


# class A:
#     num = 10


# class B(A):
#     pass


# class C(A):
#     num = 1


# class D(C, B):
#     pass


# print(D.num)  # 1
# print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# the order is D, B, C, A, object
# D inherits from B and C, B and C inherit from A, A inherits from object
# the order is determined by the order of the classes in the class definition
# if we switch B and C, the order will change
# i.e if we have class D(C, B), the order will be D, C, B, A, object

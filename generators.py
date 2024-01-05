from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
    return wrapper


@performance  # this is the decorator
def long_time():
    print('1')
    for i in range(100000000):
        i*5


@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i*5


# # long_time()
# # long_time2()


def gen_fun(num):   # this is a generator
    for i in range(num):
        yield i


# # for item in gen_fun(1000):
# #     print(item)


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


# special_for([1, 2, 3])

class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


# gen = MyGen(0, 100)
# for i in gen:
#     print(i)


# Fibonacci Numbers

def fib(num):
    a = 0
    b = 1
    for _ in range(num+1):
        yield a
        temp = a
        a = b
        b = temp + b


@performance
def fibPrint(num):
    for i in fib(num):
        print(i)


# fibPrint(1000)


def fibLi(num):
    fib = [0, 1]
    if (num <= 0):
        raise ValueError('Non-negative numbers required')
    for i in range(num-1):
        fib.append(fib[i]+fib[i+1])
    return fib


# print(fibLi(1000))

class A():
    pass


a = A
print(a)

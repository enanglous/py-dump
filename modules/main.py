# from utility import *     # bad practice (causes confusion as we don't know what we are importing)
import utility  # OR from utility import multiply, divide
# import shopping_cart (module) from shopping (package)
from shopping import shopping_cart

print(__name__)


def main():
    print(shopping_cart.buy('apple'))


if __name__ == '__main__':
    main()


'''
Def main if name main is an idiom for python scripts.
It tells what files are scripts and what aren't.
Good Practice to use this in code.
Common structure of big python projects
'''

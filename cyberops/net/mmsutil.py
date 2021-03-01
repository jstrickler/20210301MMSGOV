"""
Some generic utilities for MMS class
"""

COLORS = ['red', 'purple', 'orange']

def main():
    print("Hi, Mom!!")
    spam()
    ham()

def spam():
    """
    Fatty pig meat and stuff we don't want to know

    :return:
    """
    print("Hello from spam()")

def _toast():
    print("   and _toast()")

def ham():
    """
    Delicious smoked ham leg
    :return:
    """
    print("Hello from ham()")
    _toast()

if __name__ == '__main__':  # if executed, not imported
    main()

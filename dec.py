

import functools
Login=False

def login_decorator(func):
    @functools.wraps(func)
    def wrapper_function():
        if Login:
            func()
        else:
            print("please login first")
            return wrapper_function

@login_decorator
def my_func():
    print("profile page")

@login_decorator
def my_dashboard():
    print("dashboard")

my_func()
#my_dashboard()
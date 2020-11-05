# Ex-93_ensure_authorized.py

'''ensure_authorized
Write a function called 'ensure_authorized' which accepts a function and returns
aonther function. The function passed to it should only be invoked if there exists
a keyword argument with a name of "role and a value of "admin". Otherwise, the
inner function should return "Unauthorized".'''
'''
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin") # "Shh! Don't tell anybody!"
show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"
'''

#Ensure Authorized Decorator Solution
from functools import wraps
 
def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin")
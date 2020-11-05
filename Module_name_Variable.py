# Module_name_Variable.py
from say_sup import say_sup

def say_hi():
    print(f"HI! My __name__ is {__name__}")

if __name__ == "__main__":
    say_hi() # HI! My __name__ is __main__

# HI! My __name__ is say_sup
# SUP! My __name__ is say_sup
# HI! My __name__ is __main__

print("\n")

say_sup()

#SUP! My __name__ is say_sup

##########

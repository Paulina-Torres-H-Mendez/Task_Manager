name=input("What is your name? ")
print("hello", name)
age=input("How old are you? ")
try:
    age=int(age) # i am trying to convert it to number
    #new_age=age/0
except ValueError:
    print("you are trying to trick me")
    print("better luck next time")
except ZeroDivisionError:
    print("you can't divide by zero")
except:
    print("something unexpected happened")
else: # this happens if no error occurred
    print("you were probably born in", 2025 - int(age))
finally:
    print("thanks for playing")
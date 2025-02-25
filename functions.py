def greet():
    """
    Simple function that just prints hello
    :return: None
    """
    print("Hello!")

def greet2(name):
    """
    Simple function that greets a person
    :param name: The name of a person
    :return: None
    """
    print(f"Hello, {name}")

greet2("Jane")


def special_operation(a=1,b=1):
    """
    Special operation is 10xa+b
    :param a: first number
    :param b: second number
    :return: value, 10a+b
    """
    return 10*a+b
print(special_operation(10,2))
print(special_operation(2,10))
result=special_operation(8,9)

print(f"the special operation for 8 and 9 is: {result}")
print(special_operation(b=8,a=9))
print(special_operation())


def bond_greet(name):
    print(f"The name is: {name}")



def bond_is_the_name(first_name="James", last_name="Bond"):
    return f"{last_name}, {first_name} {last_name}"



print(bond_is_the_name("John", "Doe"))
bond_greet(bond_is_the_name(first_name="John", last_name="Doe"))
bond_greet(bond_is_the_name())
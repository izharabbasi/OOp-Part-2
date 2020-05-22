def add(a, b):
    if(type(a) == int and type(b) == int):
        return a+b
    raise TypeError("Opps there is a issue with your value")


print(add(2, 3))

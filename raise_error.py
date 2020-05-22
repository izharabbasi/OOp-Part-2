# def add(a, b):
#     if(type(a) == int and type(b) == int):
#         return a+b
#     raise TypeError("Opps there is a issue with your value")


# print(add(2, 3))


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("You have't add sounds in subclass")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "bhow bhow"


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "meao meao"


doggy = Dog("ponny", "pug")
print(doggy.sound())

caty = Cat("sunny", "russian")
print(caty.sound())

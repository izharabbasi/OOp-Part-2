class Phone:
    def __init__(self, make, model, _price):
        self.make = make
        self.model = model
        self._price = _price

    def make_call(self, number):
        print(f"Calling {number}")

    def full_name(self):
        return f"{self.make} {self.model} and price is {self._price}"


class SmartPhone(Phone):
    def __init__(self, make, model, _price, ram, memory, camera):
        super().__init__(make, model, _price)
        self.ram = ram
        self.memory = memory
        self.camera = camera


phone = Phone("Nokia ", "1100", 1000)
smartPhone = SmartPhone("iphone", "7plus", 6500, "4GB", "128GB", "12MP")

print(smartPhone.make)
print(smartPhone._price)
print(smartPhone.full_name())

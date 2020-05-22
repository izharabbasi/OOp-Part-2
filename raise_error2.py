class Mobile:
    def __init__(self, name):
        self.name = name


class MobStore:
    def __init__(self):
        self.mobile = []

    def add_phone(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobile.append(new_mobile)
        else:
            raise TypeError("you cannot pass ")


phone = Mobile("one plus")
samsung = "s8"

mobile_store = MobStore()
mobile_store.add_phone(phone)
print(mobile_store.mobile)

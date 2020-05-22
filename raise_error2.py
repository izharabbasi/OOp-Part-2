class Mobile:
    def __init__(self, name):
        self.name = name


class MobStore:
    def __init__(self):
        self.mobile = []

    def add_phone(self, new_mobile):
        return self.mobile.append(new_mobile)


phone = Mobile("one plus")
print(phone.name)

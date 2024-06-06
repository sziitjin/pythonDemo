class Father:
    name = 'jim'
    age = 38
    sex = 'man'

    def __init__(self, name):
        self.name = name

    def get_sex(self):
        return self.sex

    def speak(self):
        print('my name is {0}, age is {1}, sex is {2}'.format(self.name, self.age, self.sex))


class Son(Father):
    name = 'suk'

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def get_name(self):
        return self.name


obj = Son('jin')
obj.age = 18
obj.speak()

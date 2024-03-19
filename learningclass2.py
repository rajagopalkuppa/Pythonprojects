class AnimalTypes:
    def __init__(self, type1):
        self.type1 = type1
        print(type1)

    def animal(self):
        print("Dog")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_type1(self, type1):
        self.type1 = type1

    def get_type1(self):
        return self.type1


dog = AnimalTypes("domestic")
print(dog)
dog.animal()

lion = AnimalTypes("Wild")
lion.set_name("Lioness")
print(lion.get_name())

lion.set_type1("Jungle")
print(lion.get_type1())

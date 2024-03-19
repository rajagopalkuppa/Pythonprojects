class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old!!")


class Dog(Animal):
    def speak(self):
        print("bark")


class Cat(Animal):
    def speak(self):
        print("Meow")


pet = Animal("Dog", 12)
pet.show()

dog = Dog("Labrador", 10)
dog.show()

cat = Cat("Pussy Cat", 5)
cat.show()

cat.speak()
dog.speak()

class Dog:
    def greet(self):
        print('Bark Bark!')


class Cat:
    def greet(self):
        print('Meow Meow!')


class Person:
    def greet(self):
        print('Hello!')


finn = Dog()
murr = Cat()
me = Person()

for mammal in (finn, murr, me):
    mammal.greet()

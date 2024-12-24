# Родительский класс
class Mammal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Mammal(name={self.name})'

    def sound(self):
        print('...')

    def eat(self):
        print(f'{self.name} eats')
        self.sound()


# Дочерний класс
class Monkey(Mammal):
    def __init__(self, name, species):
        # super() == self as parent class (Mammal)
        super().__init__(name)
        self.species = species

    def __repr__(self):
        return f'Monkey(name={self.name}, species={self.species})'

    def sound(self):
        print('Hoo hoo hah!')


class Dog:
    def greet(self):
        print('Bark Bark!')


class Cat:
    def greet(self):
        print('Meow Meow!')


class Person:
    def greet(self):
        print('Hello!')

mammal = Mammal('Бабуин')
print(mammal.name)
print(mammal)
mammal.eat()

monkey = Monkey('Абу', 'Шимпанзе')
print(monkey.name)
print(monkey)
monkey.sound()
monkey.eat()

finn = Dog()
murr = Cat()
me = Person()

for mammal in (finn, murr, me):
    mammal.greet()

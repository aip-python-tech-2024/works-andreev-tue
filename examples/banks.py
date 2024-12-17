class Client:
    def __init__(self, name, initial_balance):
        self.__name = name
        self.__balance = initial_balance

    def __repr__(self):
        return f'<Client {self.__name}, balance: {self.__balance}>'

    # Свойство с геттером и сеттером
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            print('Name must be a string')

        # Убираем начальные и конечные пробелы
        name = name.strip()

        if name == '':
            print('Name cannot be empty')

        self.__name = name

    # Геттер и сеттер в явном виде
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not isinstance(name, str):
            return False

        # Убираем начальные и конечные пробелы
        name = name.strip()

        if name == '':
            return False

        self.__name = name

    def get_balance(self):
        return self.__balance

    def send_to(self, receiver, amount):
        if amount > self.__balance:
            # В идеале выкинуть исключение
            return False

        if not isinstance(receiver, Client):
            return False

        self.__balance -= amount
        receiver.__balance += amount


me = Client('Bakasa', 100)
friend = Client('Dewili', 200)
print(me, friend)

me.send_to(friend, 150)
print(me, friend)

friend.send_to(me, 150)
print(me, friend)

print(me.get_balance())
print(friend.get_balance())

me.set_name('  TEST ')
print(me)

me.set_name(me.get_name() + ' Andreev')
friend.set_name(friend.get_name() + ' Andreev')

print(me.name)
print(friend.name)

# me.name = (2. Срабатывает сеттер) me.name (1. Срабатывает геттер) + ' Andreev'
me.name += ' Andreev'
friend.name += ' Andreev'

print(me.name)
print(friend.name)

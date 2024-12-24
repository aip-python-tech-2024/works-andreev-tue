from datetime import datetime


class PassportInfo:
    def __init__(self, passport_serial, passport_number, issued_at):
        self.__passport_serial = passport_serial
        self.__passport_number = passport_number
        self.__issued_at = issued_at

    def __repr__(self):
        return f'{self.__passport_serial} {self.__passport_number} ({self.__issued_at})'


class Client:
    def __init__(self, name, passport_info, initial_balance):
        self.__name = name
        self._passport_info = passport_info
        self._balance = initial_balance

    def __repr__(self):
        return f'<Client {self.__name}, balance: {self._balance}, passport: {self._passport_info}>'

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
        return self._balance

    def send_to(self, receiver, amount):
        if amount > self._balance:
            # В идеале выкинуть исключение
            return False

        if not isinstance(receiver, Client):
            return False

        self._balance -= amount
        receiver._balance += amount

    def pay_for_maintenance(self):
        amount = 10
        if amount > self._balance:
            print('Not enough balance for account maintenance')
            return False
        self._balance -= amount


class VipClient(Client):
    def __init__(self, name, passport_info, initial_balance):
        super().__init__(name, passport_info, initial_balance)

    def pay_for_maintenance(self):
        amount = 5
        if amount > self._balance:
            print('Not enough balance for account maintenance')
            return False
        self._balance -= amount


my_passport = PassportInfo('1234', '567890', datetime.now())
me = Client('Bakasa', my_passport, 100)

friends_passport = PassportInfo('9876', '543210', datetime.now())
friend = VipClient('Dewili', friends_passport, 200)
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

me.pay_for_maintenance()
friend.pay_for_maintenance()

print(me)
print(friend)

me._balance += 10000
print(me)

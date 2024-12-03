import glob
import json


class User:
    users = {}

    def __init__(self, user_id, nickname):
        self.id = user_id
        self.nickname = nickname
        self.games_list = []


    def __repr__(self):
        return f'User(id={self.id}, nickname={self.nickname})'


    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id and self.nickname == other.nickname


    def greeting(self):
        return f'Hello {self.nickname}'

    def save(self):
        with open(f'../users/{self.id}.json', 'w', encoding='utf-8') as f:
            data = {
                'user_id': self.id,
                'nickname': self.nickname,
                'games': self.games_list,
            }
            json.dump(data, f, ensure_ascii=False)


    @staticmethod
    def load(user_id):
        with open(f'../users/{user_id}.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            user = User(data['user_id'], data['nickname'])
            user.games_list = data['games']
            return user


    @staticmethod
    def load_users():
        for path in glob.iglob('../users/*.json'):
            with open(path) as file:
                data = json.load(file)
                user = User(data['user_id'], data['nickname'])
                user.games_list = data['games']
                User.users[user.id] = user



me = User(1, 'Nikolai')
clone = User(1, 'Nikolai')
print(me.greeting())

print(me == clone)
print(me == 'hello')

admin = User(2, 'Alex')
print(admin.greeting())

# print(dir(52))

User.load_users()
print(User.users)

bakasa = User.load(188031368)
bakasa.nickname = 'Bakasa'
bakasa.save()

User.load_users()
print(User.users)

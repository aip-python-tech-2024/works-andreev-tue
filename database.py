import json


def get_file(user_id):
    filename = f'users/{user_id}.json'
    try:
        with open(filename, 'x') as file:
            json.dump({}, file)
    finally:
        return open(filename, 'r')


def set_file(user_id):
    filename = f'users/{user_id}.json'
    try:
        with open(filename, 'x') as file:
            json.dump({}, file)
    finally:
        return open(filename, 'w')

def add_game(user_id, game):
    with get_file(user_id) as file:
        data = json.load(file)

    if 'games' not in data:
        data['games'] = []
    data['games'].append(game)

    with set_file(user_id) as file:
        json.dump(data, file)

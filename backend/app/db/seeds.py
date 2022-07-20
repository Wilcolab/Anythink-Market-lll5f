import random
import string

import requests


def create_user():
    user = {
        'user': {
            'username': random_char(10, 5),
            'email':
            f"{random_char(7,3 )}@{random_char(5,3)}.{random_char(3,2)}",
            'password': random_char(20, 8)
        }
    }

    response = requests.post('http://localhost:3000/api/users', json=user)
    if response.status_code == 201:
        return True
    return False


def create_item():
    item = {
        'item': {
            'title': random_char(10),
            'description': random_char(20),
            'image': "",
            'tagList': [random_char(5) for _ in range(random.randint(0, 5))]
        }
    }

    response = requests.post(
        'http://localhost:3000/api/items',
        json=item,
        headers={
            'authorization':
            'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJleHAiOjE2NTg5NDgyNDAsInN1YiI6ImFjY2VzcyJ9.9-rxtfkqLvjtktaPS7MUmMGh9ju9uGacRUSEDAcOn3I'
        })
    if response.status_code == 201:
        return True
    return response.content


def get_items():
    request = requests.get(
        'http://localhost:3000/api/items?limit=1000&offset=0',
        headers={
            'authorization':
            'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJleHAiOjE2NTg5NDgyNDAsInN1YiI6ImFjY2VzcyJ9.9-rxtfkqLvjtktaPS7MUmMGh9ju9uGacRUSEDAcOn3I'
        })

    return [item['slug'] for item in request.json()['items']]


def post_comment(slug):
    comment = {'comment': {'body': random_char(100, 5)}}

    response = requests.post(
        f'http://localhost:3000/api/items/{slug}/comments',
        json=comment,
        headers={
            'authorization':
            'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3QiLCJleHAiOjE2NTg5NDgyNDAsInN1YiI6ImFjY2VzcyJ9.9-rxtfkqLvjtktaPS7MUmMGh9ju9uGacRUSEDAcOn3I'
        })

    if response.status_code == 201:
        return True
    return response.content


def post_n_comments(n):
    slugs = get_items()

    inserted = 0
    for _ in range(n):
        if post_comment(random.choice(slugs)):
            inserted += 1

    return inserted


def random_char(max, min=1):
    char_num = random.randint(min, max)
    return ''.join(
        random.choice(string.ascii_letters) for _ in range(char_num))


for i in range(100):
    create_user()
    create_item()

post_n_comments(100)

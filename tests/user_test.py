

def test_register_validate_user(client):
    response = client.post(
        '/users', data={ 'username': 'user4',
                        'password': 'user1',
                        'name': 'Robert',
                        'email': 'user4@gmail.com' })
    assert response.status_code == 201


def test_register_validate_user2(client):
    response = client.post(
        '/users', data={ 'username': 'user5',
                        'password': 'user5',
                        'name': 'Robert',
                        'email': 'user10@gmail.com' })
    assert response.status_code == 201


def test_register_duplicate_username(client):
    response = client.post(
        '/users', data={ 'username': 'user5',
                        'password': 'user2',
                        'name': 'Robert',
                        'email': 'user212@gmail.com' })
    assert response.status_code == 400


def test_register_long_username(client):
    response = client.post(
        '/users', data={ 'username': 'user0000000000000000000000000000000000000000000000001',
                        'password': 'user2',
                        'name': 'Robert',
                        'email': 'user22@gmail.com' })
    assert response.status_code == 400


def test_register_duplicate_email(client):
    response = client.post(
        '/users', data={ 'username': 'user3',
                        'password': 'user3',
                        'name': 'Robert',
                        'email': 'user4@gmail.com' })
    assert response.status_code == 400



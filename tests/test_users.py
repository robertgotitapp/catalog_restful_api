def test_register_duplicate_user(client):
    first_response = client.post(
        '/users', data={'username': 'timothy',
                        'password': 'IloveIceCream1',
                        'name': 'Timothy Mackenzie',
                        'email': 'timothy@gmail.com'})
    assert first_response.status_code == 201

    second_response = client.post(
        '/users', data={'username': 'timothy',
                        'password': 'IloveIceCream1',
                        'name': 'Timothy Bailey',
                        'email': 'tbailey@gmail.com'})
    assert second_response.status_code == 400


def test_register_duplicate_email(client):
    first_response = client.post(
        '/users', data={'username': 'timothy',
                        'password': 'IloveIceCream2',
                        'name': 'Timothy Mackenzie',
                        'email': 'timothy@gmail.com'})
    assert first_response.status_code == 201

    second_response = client.post(
        '/users', data={'username': 'tbailey',
                        'password': 'IloveIceCream2',
                        'name': 'Timothy Bailey',
                        'email': 'timothy@gmail.com'})
    assert second_response.status_code == 400


def test_register_long_username(client):
    response = client.post(
        '/users', data={'username': 'ilikealooooooooooooooooooooooooooooooooooooooongname',
                        'password': 'LongPassword',
                        'name': 'Long Island',
                        'email': 'ilikelongname@gmail.com'})
    assert response.status_code == 400


def test_register_invalidate_password(client):
    response = client.post(
       '/users', data={'username': 'totullie',
                       'password': 'aaaa222',
                       'name': 'Long Island',
                       'email': 'ilikelongname@gmail.com'})
    assert response.status_code == 400


def test_register_invalidate_password(client):
    response = client.post(
       '/users', data={'username': 'totukkia',
                       'password': 'aaaaaaaaaaaa',
                       'name': 'Long Island',
                       'email': 'ilikelongname@gmail.com'})
    assert response.status_code == 400


def test_register_validate_password(client):
    response = client.post(
       '/users', data={'username': 'Tojulie',
                       'password': 'Password1',
                       'name': 'Long Island',
                       'email': 'ilikelongname@gmail.com'})
    assert response.status_code == 201
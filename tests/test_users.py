def test_register_validate_user(client):
    response = client.post(
        '/users', data={'username': 'elizabeth',
                        'password': 'elizalikeicecream1',
                        'name': 'Elizabeth Mckenzie',
                        'email': 'elizamckinzie@gmail.com'})
    assert response.status_code == 201


def test_register_duplicate_email(client):
    response = client.post(
        '/users', data={'username': 'robertdaniel',
                        'password': 'robertdan20',
                        'name': 'Robert Daniel',
                        'email': 'robertdavis@gmail.com'})
    assert response.status_code == 400


def test_register_duplicate_username(client):
    response = client.post(
        '/users', data={'username': 'timothy',
                        'password': 'timothycarlos99',
                        'name': 'Timothy Carlos',
                        'email': 'timcarlos@gmail.com'})

    assert response.status_code == 400


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

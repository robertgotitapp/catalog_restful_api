import json


def test_post_validate_user(client):
    user_to_add = {'username': 'elizabeth',
                   'password': 'elizalikeicecream1',
                   'name': 'Elizabeth Mckenzie',
                   'email': 'elizamckinzie@gmail.com'}
    response = client.post(
        '/users', data=json.dumps(user_to_add), headers={'Content-type': 'application/json'})
    assert response.status_code == 201


def test_post_duplicate_email(client):
    user_to_add = {'username': 'robertdaniel',
                   'password': 'robertdan20',
                   'name': 'Robert Daniel',
                   'email': 'robertdavis@gmail.com'}
    response = client.post(
        '/users', data=json.dumps(user_to_add), headers={'Content-type': 'application/json'})
    assert response.status_code == 400


def test_post_duplicate_username(client):
    user_to_add = {'username': 'timothy',
                   'password': 'timothycarlos99',
                   'name': 'Timothy Carlos',
                   'email': 'timcarlos@gmail.com'}
    response = client.post(
        '/users', data=json.dumps(user_to_add), headers={'Content-type': 'application/json'})

    assert response.status_code == 400


def test_post_long_username(client):
    user_to_add = {'username': 'ilikealooooooooooooooooooooooooooooooooooooooongname',
                   'password': 'LongPassword',
                   'name': 'Long Island',
                   'email': 'ilikelongname@gmail.com'}
    response = client.post(
        '/users', data=json.dumps(user_to_add), headers={'Content-type': 'application/json'})
    assert response.status_code == 400


def test_post_short_username(client):
    user_to_add = {'username': 'ils',
                   'password': 'LongPassword',
                   'name': 'Long Island',
                   'email': 'ilikelongname@gmail.com'}
    response = client.post(
        '/users', data=json.dumps(user_to_add), headers={'Content-type': 'application/json'})
    assert response.status_code == 400


def test_post_invalidate_password(client):
    user_to_add = {'username': 'totullie',
                   'password': 'aaaa222',
                   'name': 'Long Island',
                   'email': 'ilikelongname@gmail.com'}
    response = client.post(
        '/users', data=json.dumps(user_to_add), headers={'Content-type': 'application/json'})
    assert response.status_code == 400


def test_post_invalidate_password(client):
    user_to_add = {'username': 'totukkia',
                   'password': 'aaaaaaaaaaaa',
                   'name': 'Long Island',
                   'email': 'ilikelongname@gmail.com'}
    response = client.post(
        '/users', data=json.dumps(user_to_add), headers={'Content-type': 'application/json'})
    assert response.status_code == 400


def test_post_validate_password(client):
    user_to_add = {'username': 'Tojulie',
                   'password': 'Password1',
                   'name': 'Long Island',
                   'email': 'ilikelongname@gmail.com'}
    response = client.post(
        '/users', data=json.dumps(user_to_add), headers={'Content-type': 'application/json'})
    assert response.status_code == 201

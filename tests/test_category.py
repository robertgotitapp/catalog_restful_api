import json


def test_register_validate_category(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                           headers={'Content-Type': 'application/json'},
                           data=json.dumps(credential)
    )
    access_token = auth_response.get_json()['access_token']

    new_category = {'description': 'Laptop, Computer, Music Player, Television.'}
    response = client.post('/categories/Lamp',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(new_category))
    assert response.status_code == 201


def test_register_duplicate_category(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                           headers={'Content-Type': 'application/json'},
                           data=json.dumps(credential)
    )
    access_token = auth_response.get_json()['access_token']

    new_category = {'description':'All items must be delicious.'}
    response = client.post('/categories/Food',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(new_category))
    assert response.status_code == 400


def test_register_long_description(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                           headers={'Content-Type': 'application/json'},
                           data=json.dumps(credential)
    )
    access_token = auth_response.get_json()['access_token']

    new_category = {'description': 'Commonly, electronic devices contain circuitry consisting primarily or'
                                   ' exclusively of active semiconductors supplemented with passive elements;'
                                   ' such a circuit is described as an electronic circuit. ... Electronics is'
                                   ' widely used in information processing, telecommunication, and signal'
                                   ' processing. Basically, electronics devices will include laptop, computer'
                                   'monitors, refrigerator, television, console, gaming machine, vacuum,'
                                   'everything around you. '}
    response = client.post('/categories/Electronics',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(new_category))
    assert response.status_code == 400


def test_get_validate_category(client):
    response = client.get('/categories/Food')
    assert response.status_code == 200


def test_get_missing_category(client):
    response = client.get('/categories/shoe')
    assert response.status_code == 404

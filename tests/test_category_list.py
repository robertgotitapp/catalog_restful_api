import json


def test_post_validate_category(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']

    new_category = {'name': 'Electronics', 'description': 'Laptop, Computer, Music Player, Television.'}
    response = client.post('/categories',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(new_category))
    assert response.status_code == 201


def test_post_duplicate_category(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']

    new_category = {'name': 'Food', 'description': 'All items must be delicious.'}
    response = client.post('/categories',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(new_category))
    assert response.status_code == 400


def test_post_long_category_name(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']

    new_category = {'name': 'Electronic Motorbike GTX-2 KEIA-2 Low Price Good Quality Only Available in 2 months',
                    'description': 'Laptop, Computer, Music Player, Television.'}
    response = client.post('/categories',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(new_category))
    assert response.status_code == 400


def test_post_short_category_name(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']

    new_category = {'name': 'Elsa',
                    'description': 'Laptop, Computer, Music Player, Television.'}
    response = client.post('/categories',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(new_category))
    assert response.status_code == 400


def test_post_long_description(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']

    new_category = {
                    'name' : 'Electronics',
                    'description': 'Commonly, electronic devices contain circuitry consisting primarily or'
                                   ' exclusively of active semiconductors supplemented with passive elements;'
                                   ' such a circuit is described as an electronic circuit. ... Electronics is'
                                   ' widely used in information processing, telecommunication, and signal'
                                   ' processing. Basically, electronics devices will include laptop, computer'
                                   'monitors, refrigerator, television, console, gaming machine, vacuum,'
                                   'everything around you. '}
    response = client.post('/categories',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(new_category))
    assert response.status_code == 400


def test_get_category_list(client):
    response = client.get('/categories?limit=2&offset=2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total_categories'] == 5
    assert len(data['categories']) == 2


def test_get_category_list_with_invalid_offset(client):
    response = client.get('/categories?limit=4&offset=6')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total_categories'] == 5
    assert len(data['categories']) == 0

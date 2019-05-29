import json


def test_post_validate_item(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_add = {
        'name': 'Macbook Air',
        'description': 'A very good laptop',
        'price': 1199.99}
    response = client.post('/categories/1/items',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(item_to_add))
    assert response.status_code == 201


def test_post_item_with_negative_price(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_add = {
        'name': 'Macbook Air',
        'description': 'A very good laptop',
        'price': -1199.99}
    response = client.post('/categories/1/items',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(item_to_add))
    assert response.status_code == 400


def test_post_item_with_long_name(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_post = {
        'name': 'Macbook Air 2017 Silver/White Color 15 inch 500GB HDD with black/white case',
        'description': 'A very good laptop. It has 13.3-inch (diagonal) LED-backlit display with IPS.',
        'price': 1199.99}
    response = client.post('/categories/1/items',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(item_to_post))
    assert response.status_code == 400


def test_post_item_with_short_name(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_post = {
        'name': 'Mac',
        'description': 'A very good laptop. It has 13.3-inch (diagonal) LED-backlit display with IPS.',
        'price': 1199.99}
    response = client.post('/categories/1/items',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(item_to_post))
    assert response.status_code == 400


def test_post_item_with_too_long_description(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_post = {
        'name': 'Macbook Air',
        'description': 'A very good laptop. It has 13.3-inch (diagonal) LED-backlit display with IPS'
                       ' technology; 2560-by-1600 native resolution at 227 pixels per inch with'
                       ' support for millions of colors. It also owns 1.6GHz dual-core Intel Core i5,'
                       ' Turbo Boost up to 3.6GHz, with 4MB L3 cache. In term of graphics, it has Intel UHD'
                       ' Graphics 617 and Support for Thunderbolt 3–enabled external graphics'
                       ' processors (eGPUs).',
        'price': 1199.99}
    response = client.post('/categories/1/items',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(item_to_post))
    assert response.status_code == 400


def test_post_item_with_invalidate_category(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_add = {
        'name': 'Macbook Air',
        'description': 'A very good laptop.',
        'price': 1199.99}
    response = client.post('/categories/10/items',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(item_to_add))
    assert response.status_code == 404


def test_post_item_with_missing_fields(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_add = {
        'description': 'A very good laptop.',
        'price': 1199.99}
    response = client.post('/categories/1/items',
                           headers=
                           {
                               'Content-Type': 'application/json',
                               'Authorization': 'JWT ' + access_token
                           },
                           data=json.dumps(item_to_add))
    assert response.status_code == 400


def test_get_item_list(client):
    response = client.get('/categories/1/items?limit=2&offset=2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total_items'] == 4
    assert len(data['items']) == 2


def test_get_item_list_with_invalid_offset(client):
    response = client.get('/categories/1/items?limit=4&offset=7')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total_items'] == 4
    assert len(data['items']) == 0

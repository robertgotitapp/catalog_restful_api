import json


def test_get_validate_item(client):
    response = client.get('/categories/1/items/1')
    assert response.status_code == 200


def test_get_missing_item(client):
    response = client.get('/categories/1/items/9')
    assert response.status_code == 404


def test_get_item_with_invalidate_category(client):
    response = client.get('/categories/2/items/1')
    assert response.status_code == 404


def test_delete_validate_item(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']

    response = client.delete('/categories/1/items/2',
                             headers=
                             {
                                 'Authorization': 'JWT ' + access_token
                             })
    assert response.status_code == 200


def test_delete_missing_item(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']

    response = client.delete('/categories/1/items/9',
                             headers=
                             {
                                 'Authorization': 'JWT ' + access_token
                             })
    assert response.status_code == 404


def test_delete_item_with_invalidate_category(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']

    response = client.delete('/categories/2/items/1',
                             headers=
                             {
                                 'Authorization': 'JWT ' + access_token
                             })
    assert response.status_code == 404


def test_delete_item_without_authorization(client):
    credential = {
        "username": "taylor",
        "password": "taylortran91"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']

    response = client.delete('/categories/1/items/2',
                             headers=
                             {
                                 'Authorization': 'JWT ' + access_token
                             })
    assert response.status_code == 403


def test_update_item_with_invalidate_category(client):
    credential = {
        "username": "taylor",
        "password": "taylortran91"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_put = {'name': 'MacbookAir', 'description': 'A very good laptop.', 'price': 1199.99}
    response = client.put('/categories/11/items/2',
                          headers=
                          {
                              'Content-Type': 'application/json',
                              'Authorization': 'JWT ' + access_token
                          },
                          data=json.dumps(item_to_put))
    assert response.status_code == 404


def test_update_item_with_missing_fields(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_put = {'description': 'A very good laptop.', 'price': 1199.99}
    response = client.put('/categories/1/items/2',
                          headers=
                          {
                              'Content-Type': 'application/json',
                              'Authorization': 'JWT ' + access_token
                          },
                          data=json.dumps(item_to_put))
    assert response.status_code == 400


def test_update_item_with_too_long_description(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_put = {'name': 'MacbookAir',
                   'description': 'A very good laptop. It has 13.3-inch (diagonal) LED-backlit display with IPS'
                                  ' technology; 2560-by-1600 native resolution at 227 pixels per inch with'
                                  ' support for millions of colors. It also owns 1.6GHz dual-core Intel Core i5,'
                                  ' Turbo Boost up to 3.6GHz, with 4MB L3 cache. In term of graphics, it has Intel UHD'
                                  ' Graphics 617 and Support for Thunderbolt 3–enabled external graphics'
                                  ' processors (eGPUs).',
                   'price': 1199.99}
    response = client.put('/categories/1/items/2',
                          headers=
                          {
                              'Content-Type': 'application/json',
                              'Authorization': 'JWT ' + access_token
                          },
                          data=json.dumps(item_to_put))
    assert response.status_code == 400


def test_update_item_without_authorization(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_put = {'name': 'MacbookAir',
                   'description': 'A very good laptop',
                   'price': 1199.99}
    response = client.put('/categories/1/items/1',
                          headers=
                          {
                              'Content-Type': 'application/json',
                              'Authorization': 'JWT ' + access_token
                          },
                          data=json.dumps(item_to_put))
    assert response.status_code == 403


def test_update_validate_item(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_put = {'name': 'MacbookAir',
                   'description': 'A very good laptop',
                   'price': 1199.99}
    response = client.put('/categories/1/items/2',
                          headers=
                          {
                              'Content-Type': 'application/json',
                              'Authorization': 'JWT ' + access_token
                          },
                          data=json.dumps(item_to_put))
    assert response.status_code == 200


def test_update_item_with_long_name(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_put = {'name': 'Macbook Air 2017 Silver/White Color 15 inch 500GB HDD with black/white case',
                   'description': 'A very good laptop',
                   'price': 1199.99}
    response = client.put('/categories/1/items/2',
                          headers=
                          {
                              'Content-Type': 'application/json',
                              'Authorization': 'JWT ' + access_token
                          },
                          data=json.dumps(item_to_put))
    assert response.status_code == 400


def test_update_item_with_short_name(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    auth_response = client.post('/auth',
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(credential)
                                )
    access_token = auth_response.get_json()['access_token']
    item_to_put = {'name': 'Ma',
                   'description': 'A very good laptop',
                   'price': 1199.99}
    response = client.put('/categories/1/items/2',
                          headers=
                          {
                              'Content-Type': 'application/json',
                              'Authorization': 'JWT ' + access_token
                          },
                          data=json.dumps(item_to_put))
    assert response.status_code == 400

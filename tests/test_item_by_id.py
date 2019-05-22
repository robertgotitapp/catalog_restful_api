import json


def test_get_validate_item(client):
    response = client.get('/categories/Laptop/items/1')
    assert response.status_code == 200


def test_get_missing_item(client):
    response = client.get('/categories/Laptop/items/9')
    assert response.status_code == 404


def test_get_item_with_invalidate_category(client):
    response = client.get('/categories/Television/items/1')
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

    response = client.delete('/categories/Laptop/items/2',
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

    response = client.delete('/categories/Laptop/items/9',
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

    response = client.delete('/categories/Television/items/1',
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

    response = client.delete('/categories/Laptop/items/2',
                             headers=
                             {
                                 'Authorization': 'JWT ' + access_token
                             })
    assert response.status_code == 403

import json


def test_authenticate_with_correct_credentials(client):
    credential = {
        "username": "robert",
        "password": "robertdavis89"
    }
    response = client.post('/auth',
                           headers={'Content-Type': 'application/json'},
                           data=json.dumps(credential)
                           )
    assert response.status_code == 200


def test_authenticate_with_incorrect_credentials(client):
    credential = {
        'username': 'timothy',
        'password': 'IloveIceCream12'
    }
    response = client.post('/auth',
                           headers={'Content-Type': 'application/json'},
                           data=json.dumps(credential)
                           )
    assert response.status_code == 401

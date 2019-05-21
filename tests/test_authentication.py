def test_authenticate_with_correct_credentials(client):
    first_response = client.post(
        '/users', data={'username': 'timothy',
                        'password': 'IloveIceCream1',
                        'name': 'Timothy Mackenzie',
                        'email': 'timothy@gmail.com'})
    assert first_response.status_code == 201

    second_response = client.post(
        '/auth', data={
            'username': 'timothy',
            'password': 'IloveIceCream1'
        }
    )
    assert second_response.status_code == 200


def test_authenticate_with_incorrect_credentials(client):
    first_response = client.post(
        '/users', data={'username': 'timothy',
                        'password': 'IloveIceCream1',
                        'name': 'Timothy Mackenzie',
                        'email': 'timothy@gmail.com'})
    assert first_response.status_code == 201

    second_response = client.post(
        '/auth', data={
            'username': 'timothy',
            'password': 'IloveIceCream12'
        }
    )
    assert second_response.status_code == 401
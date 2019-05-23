def test_get_validate_category(client):
    response = client.get('/categories/1')
    assert response.status_code == 200


def test_get_missing_category(client):
    response = client.get('/categories/10')
    assert response.status_code == 404

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

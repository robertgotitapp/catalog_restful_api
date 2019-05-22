def test_get_item_list(client):
    response = client.get('/categories/Laptop/items?limit=2&offset=2')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total_items'] == 4
    assert len(data['items']) == 2


def test_get_item_list_with_invalid_offset(client):
    response = client.get('/categories/Laptop/items?limit=4&offset=7')
    assert response.status_code == 200
    data = response.get_json()
    assert data['total_items'] == 4
    assert len(data['items']) == 0

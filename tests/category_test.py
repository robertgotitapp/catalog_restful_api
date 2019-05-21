def test_register_duplicate_category(client):
    first_response = client.post(
        '/categories', data={
                        'name': 'Electronics',
                        'description': 'Laptop, Computer, Music Player, Television.'})
    assert first_response.status_code == 201

    second_response = client.post(
        '/categories', data={
                        'name': 'Electronics',
                        'description': 'All items comes with electricity.'})
    assert second_response.status_code == 400


def test_register_long_description(client):
    response = client.post(
        '/categories', data={
                        'name': 'Electronics',
                        'description': 'Commonly, electronic devices contain circuitry consisting primarily or'
                                       ' exclusively of active semiconductors supplemented with passive elements;'
                                       ' such a circuit is described as an electronic circuit. ... Electronics is'
                                       ' widely used in information processing, telecommunication, and signal'
                                       ' processing. Basically, electronics devices will include laptop, computer'
                                       'monitors, refrigerator, television, console, gaming machine, vacuum,'
                                       'everything around you. '})
    assert response.status_code == 400
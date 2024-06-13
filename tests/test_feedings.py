def test_get_feedings(client):
    response = client.get('/feedings')
    assert response.status_code == 200

def test_get_feeding(client):
    response = client.get('/feedings/1')
    assert response.status_code == 200

def test_create_feeding(client):
    new_feeding = {
        "terminal_id": 1,
        "enclosure_id": 1,
        "food_type": "Meat",
        "feeding_time": "2024-06-13T08:00:00Z"
    }
    response = client.post('/feedings', json=new_feeding)
    assert response.status_code == 201

def test_update_feeding(client):
    updated_feeding = {
        "terminal_id": 1,
        "enclosure_id": 1,
        "food_type": "Vegetables",
        "feeding_time": "2024-06-13T10:00:00Z"
    }
    response = client.put('/feedings/1', json=updated_feeding)
    assert response.status_code == 200
    # Add more assertions based on your expected response

def test_delete_feeding(client):
    response = client.delete('/feedings/1')
    assert response.status_code == 204

def test_get_animals(client):
    response = client.get("/animals")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_animal(client):
    response = client.get("/animals/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1

def test_create_animal(client):
    new_animal = {
        "species": "Giraffe",
        "age": 4,
        "gender": "Male",
        "special_requirements": "Tall enclosure"
    }
    response = client.post("/animals", json=new_animal)
    assert response.status_code == 201
    data = response.get_json()
    assert data['species'] == "Giraffe"
def test_get_employees(client):
    response = client.get("/employees")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_employee(client):
    response = client.get("/employees/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1

def test_create_employee(client):
    new_employee = {
        "name": "Alice Wonderland",
        "email": "alice@example.com",
        "phone": "111-222-3333",
        "role": "Tour Guide",
        "schedule": "9-5"
    }
    response = client.post("/employees", json=new_employee)
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == "Alice Wonderland"
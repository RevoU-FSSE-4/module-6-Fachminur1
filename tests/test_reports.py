def test_get_reports_animals(client):
    response = client.get('/reports/animals')
    assert response.status_code == 200

def test_get_reports_visitors(client):
    response = client.get('/reports/visitors')
    assert response.status_code == 200

def test_get_reports_revenue(client):
    response = client.get('/reports/revenue')
    assert response.status_code == 200

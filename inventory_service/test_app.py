import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_inventory(client):
    rv = client.get('/inventory')
    assert rv.status_code == 200
    assert b'Inventory List' in rv.data

def test_add_inventory(client):
    rv = client.post('/inventory', json={'id': 1, 'name': 'item1', 'quantity': 100})
    assert rv.status_code == 201
    assert b'item1' in rv.data

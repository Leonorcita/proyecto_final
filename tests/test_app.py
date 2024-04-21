import pytest
from app import create_app, db
from app.models import Data

@pytest.fixture
def client():
    app = create_app("testing")
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_insert_data(client):
    # Test inserting data
    response = client.post("/data", json={"name": "Test Data"})
    assert response.status_code == 200
    assert response.json["message"] == "Data inserted successfully"

def test_get_all_data(client):
    # Test getting all data
    response = client.get("/data")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_delete_data(client):
    # Test deleting data
    response = client.delete("/data/1")
    assert response.status_code == 404  # Assuming no data with ID 1 exists initially

def test_manage_py(capsys):
    import os
    os.environ["FLASK_ENV"] = "testing"
    import manage  # Importa manage.py para ejecutar su código
    # Agrega aserciones para verificar que las tablas de la base de datos se crean correctamente
    captured = capsys.readouterr()
    assert "Database tables created." in captured.out

def test_run_py():
    import os
    os.environ["FLASK_ENV"] = "testing"
    import run  # Importa run.py para ejecutar su código
    # Agrega aserciones para verificar que la aplicación se está ejecutando correctamente
    # Por ejemplo, puedes hacer una solicitud HTTP a la aplicación y verificar la respuesta
    with run.app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200

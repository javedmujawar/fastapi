from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#test home api
def test_home():
    response = client.get("/")
    #status code
    assert response.status_code ==200
    # response data
    assert response.json() == {"message":"Hello Javed"}

#Test add api
def test_add():
    response = client.get("/add?a=10&b=20")
    assert response.status_code ==200
    assert response.json()=={"result":30}

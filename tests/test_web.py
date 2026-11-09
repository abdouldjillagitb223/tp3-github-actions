from app.web import create_app
import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_scode_200(client):
    resultat=client.post(
        "/moderate", 
        json={"message": "bonjour"}
        )
    assert resultat.status_code==200
    assert resultat.get_json()=={"decision": "autoriser"}
    
def test_scode_spam(client):
    reponse=client.post(
        "/moderate",
        json={"message": "ceci est du SPAM"}
    )
    
    assert reponse.status_code==200
    assert reponse.get_json()=={"decision":"bloquer"}
    
def test_scode400v(client):
    reponse=client.post(
        "/moderate",
        json={}
    )
    assert reponse.status_code==400
    assert reponse.get_json()=={"error":"Invalid message"}
  
def test_scode400(client):
    reponse=client.post(
        "/moderate",
        json={"message":42}
    )
    assert reponse.status_code==400
    assert reponse.get_json()=={"error":"Invalid message"}
  
def test_scode_mv(client):
    reponse=client.post(
        "/moderate",
        json={"message":" "}
    )  

    assert reponse.status_code==400
    assert reponse.get_json()=={"error":"Invalid message"}
    
def test_scode_l(client):
    repons=client.post(
        "/moderate",
        json=["bonjour", "spam"]
    )
    
    assert repons.status_code==400
    assert repons.get_json()=={"error":"Json object required"}
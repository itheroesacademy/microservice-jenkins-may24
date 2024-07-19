import json
from index import app

def test_hello():
    with app.test_client() as client:
        response = client.get('/')
        data = json.loads(response.get_data(as_text=True))
        assert data["1"] == "Apple Iphone"
        assert data["2"] == "MacBook"
        assert data["3"] == "Your Fav Something else"

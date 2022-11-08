
def test_get_all_planets_with_db_return_empty_list(client):
    response = client.get("/planet")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_with_empty_db_returns_404(client):
    response = client.get("/planet/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert "message" in response_body

def test_get_one_planet_with_populated_db_returns_planet_json(client, two_planets):
    response = client.get("/planet/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == { 
        "id": 1,
        "name": "Mercury", 
        "description": "Closest planet to sun, in the Milky Way Galaxy. Mercury has no moons and has a thin atmosphere.", 
        "type": "terrestrial"
        }

def test_post_one_planet_creates_planet_with_new_id_in_db(client):
    response = client.post("/planet", json={
        "name": "Mercury", 
        "description": "Closest planet to sun, in the Milky Way Galaxy. Mercury has no moons and has a thin atmosphere.", 
        "type": "terrestrial"
    })
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert "id" in response_body
    assert response_body["id"] == 1
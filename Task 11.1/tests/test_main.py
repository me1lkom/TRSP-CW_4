class TestCreateUser:
    def test_create_user_success(self, client, clear_db):
        response = client.post(
            "/users",
            json={"username":"lev", "age":20}    
        )
        assert response.status_code == 201
        data = response.json()
        assert "id" in data 
        assert data["username"] == "lev"
        assert data["age"] == 20
    
    def test_create_user_fail(self, client, clear_db):
        response = client.post(
            "/users",
            json={"username":"lev", "age":"s"}
        )
        assert response.status_code == 422
        
        
class TestGetUser:
    def test_get_user_success(self, client, clear_db):
        create_user = client.post("/users", json={"username":"lev", "age":20})
        user_id = create_user.json()["id"]
        
        response = client.get(f"/users/{user_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "lev"
        assert data["age"] == 20
    
    def test_get_user_fail(self, client, clear_db):
        response = client.get("/users/100")
        assert response.status_code == 404
        assert response.json()["detail"] == "User not found"
        
    
class TestDeleteUser:
    def test_delete_user_success(self, client, clear_db):
        create_user = client.post("/users", json={"username":"lev", "age":20})
        user_id = create_user.json()["id"]
        
        response = client.delete(f"/users/{user_id}")
        assert response.status_code == 204
        assert response.text == ""
        
    def test_delete_user_fail(self, client, clear_db):
        response = client.delete("/users/100")
        assert response.status_code == 404
        assert response.json()["detail"] == "User not found"

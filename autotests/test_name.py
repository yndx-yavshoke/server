import requests

URL = "http://localhost:3000" 


def test_name_update():     # новое имя 

    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjEsImlhdCI6MTc1MTM0NjMyMSwiZXhwIjoxNzUxNDMyNzIxfQ.F_6Hp1lsemIjdgmPHqk7rKy9svk-ColHNjI9DGhwLOs"
    headers = {
        "Authorization": f"Bearer {token}",
    }

    responseMeMethod = requests.get(f"{URL}/user/me", headers=headers) # выполнение метода со информацией о себе для сравнения
    response = requests.patch(f"{URL}/user/name", headers=headers, json={"name": "new_name"}) # изменение имени
    
    assert response.status_code == 200   # код ответа = 200

    response_data = response.json()               # cохранение ответа на изменение имя в формате json
    user_data = response_data["user"]             # сохранение словаря user в user_data
    response_dataMe = responseMeMethod.json()     # сохранение ответа в методе /user/me в формате json
    user_dataMe = response_dataMe["user"]         # сохранение словаря user в user_dataMe

    assert user_data["name"] == "new_name"              # имя совпадает новому
    assert user_data["id"] == user_dataMe["id"]           # id совпадает старому
    assert user_data["email"] == user_dataMe["email"]     # email совпадает старому
    assert user_data["age"] == user_dataMe["age"]         # age совпадает старому

    # меняем имя на старое для будущих прогонов:
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjEsImlhdCI6MTc1MTM0NjMyMSwiZXhwIjoxNzUxNDMyNzIxfQ.F_6Hp1lsemIjdgmPHqk7rKy9svk-ColHNjI9DGhwLOs"
    headers = {
        "Authorization": f"Bearer {token}",
    }   
    requests.patch(f"{URL}/user/name", headers=headers, json={"name": "old_name"})                    


def test_name_update_with_wrong_token():           # неправильный токен
    token = "null"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    response = requests.patch(f"{URL}/user/name", headers=headers, json={"name": "new_name"}) 

    assert response.status_code == 401                    # код ответа = 401


def test_name_update_validation_error():           # некорректное имя
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjEsImlhdCI6MTc1MTM0NjMyMSwiZXhwIjoxNzUxNDMyNzIxfQ.F_6Hp1lsemIjdgmPHqk7rKy9svk-ColHNjI9DGhwLOs"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    response = requests.patch(f"{URL}/user/name", headers=headers, json={"name": ""}) 

    assert response.status_code == 422                   # код ответа = 422
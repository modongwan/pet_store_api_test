from http.client import responses

import faker
import pytest
import requests
from main_data.pet import pet_dict
from faker import Faker

faker = Faker("en_US")

def test_create_pet(url, delete_pet):
    response = requests.post(url + f"/pet",  json=pet_dict)
    assert response.status_code == 200
    if response.status_code == 200:
        pet_data = response.json()
        print("")
        print(f"ID: {pet_data["id"]}")
        print(f"Name: {pet_data["name"]}")
        print(f"Status: {pet_data["status"]}")
    else:
        print("NO SUCCESS")
    delete_pet(response.json()["id"])



def test_find_by_id(url, create_pet):
    pet_id = create_pet
    response = requests.get(url + f"/pet/{pet_id}")
    if response.status_code == 200:
        pet_data = response.json()
        print("")
        print(f"Name: {pet_data["name"]}")
        print(f"Name: {pet_data["id"]}")
        print(f"Name: {pet_data["status"]}")
    else:
        print("NO SUCCESS")


@pytest.mark.parametrize("status", ["availalbe", "sold", "pending", "null"])
def test_find_pet_by_status(url, status):
    parametres = {"status" : status}
    response = requests.get(url + "/pet/findByStatus", params=parametres)
    assert response.status_code == 200
    status_data = response.json()
    for item in status_data:
        assert "id" in item
        assert item["id"]


def test_update_pet_name(url, create_pet):
   pet_id = create_pet
   update_name = faker.first_name()
   before_response = requests.get(url +f"/pet/{pet_id}")
   before_data = before_response.json()
   if before_response.status_code == 200:
       print("")
       print(f"Name: {before_data["name"]}")
   else:
       print("PET DIDN'T CREATED")

   name_update = {
        "id": pet_id,
        "name": update_name,
        "status": "available"
   }

   response = requests.put(url + "/pet", json=name_update)
   assert response.status_code == 200
   pet_data = response.json()

   if response.status_code == 200:
       print("")
       print(f"Updated Name: {pet_data["name"]}")
   else:
       print("NAME DIDNT UPDATED")


def test_delete_pet(url, create_pet):
    pet_id = create_pet
    before_delete_pet = requests.get(url + f"/pet/{pet_id}")
    before_delete_pet_data = before_delete_pet.json()
    if before_delete_pet.status_code == 200:
        print("")
        print(f"Name: {before_delete_pet_data["name"]}")
        print(f"ID: {before_delete_pet_data["id"]}")
        print(f"Status: {before_delete_pet_data["status"]}")
    response = requests.delete(url + f"/pet/{pet_id}")
    assert response.status_code == 200
    if response.status_code == 200:
        print("PET WAS SUCCESSFULLY DELETED")


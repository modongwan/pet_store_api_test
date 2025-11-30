from http.client import responses

import requests
from main_data.user import user_dict
import pytest



def check_deleted_user(url, username):
    response = requests.get(url + f"/user/{username}")
    if response.status_code == 404:
        print("User_deleted")
    else:
        print("He is still among us")


def test_create_user(url, delete_user):
    response = requests.post(url + f"/user", json=user_dict)
    print(user_dict["username"])
    if response.status_code == 200:
       user_id = response.json()["message"]
       print(f"User was created, USER ID: {user_id}")
    else:
        print("USER DIDN'T CREATED")
    delete_user(user_dict.get("username"))
    check_deleted_user(url, user_dict["username"])



def test_create_userList(url, delete_user):
    user_array = [user_dict]
    print(user_array)
    response = requests.post(url + "/user/createWithList", json=user_array)
    assert response.status_code == 200
    delete_user(user_dict["username"])
    check_deleted_user(url,user_dict["username"])

def test_find_by_username(url, create_user):
    username = create_user
    response = requests.get(url + f"/user/{username}")
    assert response.status_code == 200


def test_user_login(url, create_user_for_login):
    user = create_user_for_login
    (login, password) = (user["username"],user["password"])
    response = requests.get(url+f"/user/login?{login}&{password}")
    assert response.status_code == 200
    print("User logged successfully")
    requests.get(url+"/user/logout")


def test_user_logout(url):
    response = requests.get(url + "/user/logout")
    assert response.status_code == 200

def test_fff(url):
    check_deleted_user(url, "ziminasvetlana")



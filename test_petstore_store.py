from http.client import responses

import requests
import pytest
from main_data.store import order_dict

def test_get_inventory(url):
    response = requests.get(url + f"/store/inventory/")
    print(response.text)
    assert response.json()["available"]
    assert response.json()["sold"]
    assert response.status_code == 200


def test_create_order(url, delete_order):
    response = requests.post(url + "/store/order", json=order_dict)
    assert response.status_code == 200
    order_data = response.json()
    if response.status_code == 200:
        print("")
        print(f"Order_id: {order_data["id"]}")
        print(f"Pet_id: {order_data["petId"]}")
    else:
        print("Order didn't made")
    delete_order(order_dict.get("id"))
    check_deleted_order(url, order_dict["id"])

def test_find_order_by_id(url, create_order):
    order_id = create_order
    response = requests.get(url + f"/store/order/{order_id}")
    order_data = response.json()
    assert response.status_code == 200
    if response.status_code == 200:
        print("")
        print(f"Order_id: {order_data["id"]}")
        print(f"Pet_id: {order_data["petId"]}")
    else:
        print("Order didn't found")

def test_delete_by_id(url, create_order):
    order_id = create_order
    response = requests.delete(url +  f"/store/order/{order_id}")
    assert response.status_code == 200
    print("Order was successfully deleted")


def check_deleted_order(url,order_id):
    response = requests.get(url + f"/store/order/{order_id}")
    if response.status_code == 404:
        print("Order Data deleted")
    else:
        print("Order Data didn't deleted")
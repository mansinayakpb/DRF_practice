import json

import requests

URL = "http://127.0.0.1:8443/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# class DataFetcher:
#     def __init__(self, url):
#         self.url = url

#     def get_data(self, id=None):
#         data = {}
#         if id is not None:
#             data = {'id': id}
#         json_data = json.dumps(data)
#         r = requests.get(url=self.url, data=json_data)
#         response_data = r.json()
#         print(response_data)

# get_data()

# def post_data():
#     data = {
#         'name': 'Sobit',
#         'roll': 205,
#         'city': 'Indore',
#     }

#     json_data = json.dumps(data)
#     r = requests.post(url=URL, data=json_data)
#     data = r.json()
#     print(data)


# post_data()


def post_data():
    data = {
        "name": "Rohan",
        "roll": 120,
        "city": "Bhopal",
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


post_data()


def update_data():
    data = {"id": 2, "name": "test", "city": "Indore"}

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


# update_data()


def delete_data():
    data = {"id": 4}

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


# delete_data()

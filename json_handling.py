import json

FILE_NAME = "users.json"

def get_users():
    with open("users.json", "r") as file:
        users = json.load(file)
        return users
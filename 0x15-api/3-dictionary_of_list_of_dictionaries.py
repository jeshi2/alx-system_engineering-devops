#!/usr/bin/python3
"""extend your Python script to
export data in the JSON format"""
import json
import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()

all_data = {}

for user in users:
    user_id = str(user['id'])
    username = user['username']

    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    tasks = response.json()

    user_tasks = [{"username": username, "task": task['title'],
                   "completed": task['completed']} for task in tasks]

    all_data[user_id] = user_tasks

# Export to JSON file
with open("todo_all_employees.json", "w") as outfile:
    json.dump(all_data, outfile)

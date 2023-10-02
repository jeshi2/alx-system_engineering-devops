#!/usr/bin/python3
"""Python script to export data in the JSON format"""
import csv
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Define the API endpoint URL
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    """Fetch employee's todo list"""
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a dictionary for the JSON data
    json_data = {str(user_data['id']): []}

    # Populate the JSON data with task information
    for todo in todos_data:
        task_info = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user_data['username']
        }
        json_data[str(user_data['id'])].append(task_info)

    # Create a JSON file for the user
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

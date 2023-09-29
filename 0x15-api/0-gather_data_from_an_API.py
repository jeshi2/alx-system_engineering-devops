#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Define the API endpoint URL"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate the number of completed tasks and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    # Display the employee's TODO list progress
    print(
        "Employee {} is done with tasks({} / {}): ".format(
            user_data['name'], completed_tasks, total_tasks
        )
    )

    # Display the titles of completed tasks
    for todo in todos_data:
        if todo["completed"]:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

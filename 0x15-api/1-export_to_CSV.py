#!/usr/bin/python3
"""
Python script to export data in the CSV format
"""
import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    # Define the API endpoint URL
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a CSV file for the user
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write task data to the CSV file
        for todo in todos_data:
            csv_writer.writerow([user_data['id'], user_data['username'],
                                 todo['completed'], todo['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

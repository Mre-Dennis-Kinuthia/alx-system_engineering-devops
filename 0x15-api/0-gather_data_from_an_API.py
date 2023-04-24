#!/usr/bin/python3
"""Gather data from API"""

import requests
from sys import argv

def get_employee_info(employee_id):
    """
    Given an employee ID, retrieves the employee's name and the number of tasks completed
    out of the total number of tasks.
    """
    # Make a GET request to the API to retrieve the employee data
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)

    # If the response is not successful, raise an exception
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve employee data: {response.content}")

    # Parse the JSON response to get the employee's name
    employee_name = response.json()["name"]

    # Make another GET request to retrieve the employee's TODO list
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)

    # If the response is not successful, raise an exception
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve employee TODO list: {response.content}")

    # Count the number of completed tasks and the total number of tasks
    tasks = response.json()
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task["completed"]])

    return employee_name, completed_tasks, total_tasks

def print_employee_todo_list(employee_id):
    """
    Given an employee ID, retrieves and prints the employee's TODO list progress.
    """
    employee_name, completed_tasks, total_tasks = get_employee_info(employee_id)

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    # Make another GET request to retrieve the employee's TODO list
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)

    # If the response is not successful, raise an exception
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve employee TODO list: {response.content}")

    # Print the title of each completed task
    tasks = response.json()
    for task in tasks:
        if task["completed"]:
            print("\t " + task["title"])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    print_employee_todo_list(employee_id)

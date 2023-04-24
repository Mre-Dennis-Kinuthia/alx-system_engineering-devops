#!/usr/bin/python3
"""
Script that, using this REST API,
exports information about the TODO list progress
for a given employee ID in CSV format
"""
import csv
import requests
from sys import argv


def export_employee_todo_list_csv(emp_id):
    """
    Script that, using this REST API,
    for a given employee ID, returns information
    about the TODO list progress and exports it to a CSV file.

    Usage: ./2-export_to_CSV.py <emp_id>

    The script exports a CSV file with the following format:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

    he filename of the exported CSV file is "<emp_id>.csv".
    """
    employee_url = "https://jsonplaceholder.typicode.com/users/" + emp_id
    tsk_url = "https://jsonplaceholder.typicode.com/todos?userId=" + emp_id

    employee_name = (requests.get(employee_url)).json().get("name")
    tasks = requests.get(tsk_url)

    with open(emp_id + ".csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks.json():
            writer.writerow([task.get("userId"),
                             employee_name, task.get("completed"),
                             task.get("title")])
    print("CSV file exported successfully!")


if __name__ == "__main__":
    emp_id = argv[1]
    export_employee_todo_list_csv(emp_id)

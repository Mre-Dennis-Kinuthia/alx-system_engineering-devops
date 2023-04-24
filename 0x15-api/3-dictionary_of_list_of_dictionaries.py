#!/usr/bin/python3

"""Python script that uses the JSONPlaceholder API
to retrieve information about all tasks from all employees
and export them to a JSON file."""

import json
import requests
import sys


def export_tasks_to_json():
    """ Get all employees"""
    employees_url = 'https://jsonplaceholder.typicode.com/users'
    employees = requests.get(employees_url).json()

    """ Initialize a dictionary to store tasks by employee"""
    tasks_by_employee = {}

    """Get tasks for each employee"""
    for employee in employees:
        emp_id = employee['id']
        tsk_url = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'
        tasks = requests.get(tsk_url).json()

        """ Add tasks to the dictionary """
        tasks_by_employee[emp_id] = []
        for task in tasks:
            task_dict = {
                'username': employee['username'],
                'task': task['title'],
                'completed': task['completed']
            }
            tasks_by_employee[emp_id].append(task_dict)

    """ Export tasks to a JSON file """
    with open('todo_all_employees.json', mode='w') as json_file:
        json.dump(tasks_by_employee, json_file)


if __name__ == '__main__':
    export_tasks_to_json()

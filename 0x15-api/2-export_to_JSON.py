#!/usr/bin/python3
""" Export data in the JSON format """

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    response = requests.get(url)
    employee_name = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + user_id
    response = requests.get(url)
    tasks = response.json()

    tasks_list = []
    for task in tasks:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = employee_name
        tasks_list.append(task_dict)

    export_dict = {}
    export_dict[user_id] = tasks_list
    filename = user_id + ".json"
    with open(filename, "w") as json_file:
        json.dump(export_dict, json_file)

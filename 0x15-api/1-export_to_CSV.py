#!/usr/bin/python3
"""Python script that, using this REST API,
    for a given employee ID, returns information about
    his/her TODO list progress and exports it to a CSV file"""

import csv
import requests
from sys import argv


def export_employee_todo_list_csv(employee_id):
    """export data to csv file"""
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()
    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)).json()

    # prepare data for csv file
    data = []
    for task in todo_list:
        task_data = [str(employee_id),
                     user_data['username'],
                     str(task['completed']),
                     task['title'].replace(',', '')]
        data.append(task_data)

    # write data to csv file
    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for row in data:
            writer.writerow(row)

    print('Employee {}\'s tasks saved to {}'.format(employee_id, filename))


if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ./1-export_to_CSV.py <employee_id>')
        exit(1)

    try:
        emp_id = int(argv[1])
    except ValueError:
        print('Employee ID must be an integer')
        exit(1)

    export_employee_todo_list_csv(emp_id)

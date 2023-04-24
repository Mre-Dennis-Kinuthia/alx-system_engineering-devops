import json
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) == 2 and argv[1].isdigit():
        user_id = argv[1]
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        response = requests.get(url)
        if response.status_code == 200:
            user_info = json.loads(response.text)
            name = user_info.get('name')
            url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
            response = requests.get(url)
            if response.status_code == 200:
                tasks = json.loads(response.text)
                total_tasks = len(tasks)
                completed_tasks = [task.get('title') for task in tasks if task.get('completed')]
                print("Employee {} is done with tasks({}/{}):".format(name, len(completed_tasks), total_tasks))
                for task in completed_tasks:
                    print("\t {}".format(task))

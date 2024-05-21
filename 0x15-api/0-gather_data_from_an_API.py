#!/usr/bin/python3
"""This script consumes an API to retrieve todos by user ID
and returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user_response = requests.get(f'{base_url}users/{user_id}')
    user = user_response.json()
    todos_response = requests.get(f'{base_url}todos', params={'userId': user_id})
    todos = todos_response.json()
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{len(todos)}):")
    for title in completed_tasks:
        print(f"\t {title}")


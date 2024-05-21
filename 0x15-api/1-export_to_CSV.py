#!/usr/bin/python3
"""Script to export user TODO data to a CSV file."""
import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    
    user_url = f"{base_url}users/{user_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

   
    todos_url = f"{base_url}todos"
    todos_response = requests.get(todos_url, params={"userId": user_id})
    todo_data = todos_response.json()

    
    filename = f"{user_id}.csv"
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            writer.writerow([user_id, username, todo.get("completed"), todo.get("title")])


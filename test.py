import requests
import json

if __name__ == "__main__":
    base_url="http://127.0.0.1:80/"

    todo_item_extension = "todo_item"
    is_alive_extension = "api/check-status"
    todo_items_extension = "todo_items"

    payload = {"task_description" : "test_item"}

    # check if alive
    r = requests.get(base_url+is_alive_extension)

    # Post a todo-item
    r = requests.post(base_url+todo_item_extension,
                      headers = {"Content-Type": "application/json"},
                      data=json.dumps(payload))

    # get all todo-items
    r = requests.get(base_url+todo_items_extension)
    print(r.text)
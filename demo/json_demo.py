import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)

#todos_string = json.dumps(todos, indent=4)
#with open("todos.json", "w") as write_file:
#    json.dump(todos, write_file)
#todos_string = json.dumps(todos, indent = 4)

#There are multiple users, each with a unique userId, and each task has a Boolean completed property. Can you determine which users have completed the most tasks?

#ein dict du mongo -_-
todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]] = 1


top_users = sorted(todos_by_user.items(), key = lambda item: item[1], reverse=True)

max_complete = top_users[0][1]
#print(max_complete)

winners = []

for key, value in top_users:
    if value < max_complete:
        break
    winners.append(str(key))

max_users = " and ".join(winners)

#print(f"users {max_users} completed {max_complete} todos")
print(winners)

# Define a function to filter out completed TODOs of users with max completed TODOS.

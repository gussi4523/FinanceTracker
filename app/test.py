import json
class User():
    name: str
    email: str

user = User()
user.name = "John"
user.email = "Tts"

with open("users.json","r") as file:
    data = json.load(file)

if not any (u["email"] == user.email for u in data):
    with open("users.json","w") as file:
        # Example: Loading from a string
        jsData = {"name": user.name, "email":user.email}
        data.append(jsData)
        json.dump(data,file,indent=4)
else:
    print("User exist")

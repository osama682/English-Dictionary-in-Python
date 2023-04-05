import json
data = json.load(open("data.json"))

def translate(a):
    return data[a]

b = input("Enter word : ")
print(translate(b))

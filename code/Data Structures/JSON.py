import json
from json import JSONEncoder

person = {"name": "John",
          "city": "New York",
          "age": 30,
          "hasChildren": False,
          "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)  # Convert dictionary to json
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4, sort_keys=True)  # Write json to file

person = json.loads(personJSON)  # Convert json to dictionary
print(person)

with open('person.json', 'r') as file:
    person = json.loads(personJSON)  # Read json from file
    print(person)


class User:  # custom object

    def __init__(self, name, age):
        self.name = name
        self.age = age


def encode_user(o):  # custom object encoding function
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


user = User('Max', 27)
userJSON = json.dumps(user, default=encode_user)    # Convert custom object to json
print(userJSON)


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


userJSON = json.dumps(user, cls=UserEncoder)        # Convert custom object to json
print(userJSON)
userJSON = UserEncoder().encode(user)               # Convert custom object to json
print(userJSON)

user = json.loads(userJSON)                         # Converts json to dictionary
print(user)


def decode_user(dct):   # custom object decoding function
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


user = json.loads(userJSON, object_hook=decode_user)                         # Converts json to custom object
print(type(user))
print(user.name)

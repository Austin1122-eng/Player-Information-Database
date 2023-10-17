import json

class Person:
    def __init__(self, name):
        self.name = name
        self.cars = []
    def to_json(self):
        carInstance = car('350')
        self.cars.append(carInstance)
        return{
            'name' : self.name,
            'cars': self.cars
        }

class car:
    def __init__(self, model):
        self.model = model


john = Person('John')

json_str = json.dumps(john.to_json())
print(json_str)


# print(json.dumps(john.__dict__))
# x = {
#     "name": "John",

#     "cars": [
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford Edge", "mpg": 24.1}
#     ]
# }

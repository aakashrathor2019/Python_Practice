#Example of using a dictionary in Python for updating and accessing values
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

# Dictionary Example with multiple methods
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.items())
x = car.items()
print(car)
print(id(car))
print(id(x))

car["year"] = 2018
print(car)

print(x)


#Values method example
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

           
print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)
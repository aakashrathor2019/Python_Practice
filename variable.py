class Demo:
    def  __init__(self, name, age, city = None):
        self.name = name
        self.age = age
        self.city = city

    def get_data(self):
        return  f"Name of candidate is {self.name} and age is {self.age} and city is {self.city}"
    
obj = Demo("Jon", 55, "Indore")
print(obj.get_data())
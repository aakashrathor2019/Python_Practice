class Parent:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def multiply(self):
        return self.val1 * self.val2


class Child(Parent):
    def multiply(self):
        return super().multiply() * 10


obj1 = Parent(2,2)
print(f"Parent Class Method: {obj1.multiply()}")
obj = Child(2, 5)
print(f"Child Class Method: {obj.multiply()}")

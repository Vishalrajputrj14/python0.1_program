'''
Gatters and in python are methods that are used to access the valuse of an object's  properties. They aren used to reuturn the value of a soecific property and are
typically defined using the @property decorator.Here is an example of a simple class with a getter method:  

'''

class MyClass:
    def __init__(self, value):
        self._value = value  # private attribute

    def show(self):
        print(f"The value is {self._value}")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value / 10


obj = MyClass(18)
obj.show()          # The value is 18
print(obj.value)    # Accesses property -> 18
obj.value = 50      # Sets value as 50/10 = 5
obj.show()          # The value is 5

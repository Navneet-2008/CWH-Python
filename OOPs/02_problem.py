import math

class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num * self.num

    def cube(self):
        return self.num * self.num * self.num
    
    def sqroot(self):
        return math.sqrt(self.num)
    
    @staticmethod
    def greet():
        print("hello")

obj = calculator(5)

print(obj.square())
print(obj.sqroot())
print(obj.cube())
obj.greet()

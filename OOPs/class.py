class Employee:
    name = "navneet"
    age = 16
    language = "python"
    salary = 9000000

    def __init__(self,name,age,language):
        self.name = name
        self.age = age
        self.language = language
        print("good morning rajvir")

    @staticmethod
    def greet():
        print("hello")

    def getinfo(self):
        print(f"my name is {self.name}. my age is {self.age}")

navneet = Employee("navii",16,"c++")
print(navneet.language,navneet.name,navneet.age)
navneet.getinfo()

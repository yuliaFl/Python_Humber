class Person:
    def __init__(self,age,weight,height, first_name, last_name):
        self.age =age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}")
        print(f"Height: {self.height}")

person1 = Person(age=80, weight=100, height=175, first_name= "Yulia", last_name="Fl")

person1.display_info()
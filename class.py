class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"hello, i am {self.name}, {self.age} years old, and my gender is {self.gender}.")

person1 = person("john", 25, "male")

person1.introduce()
class Person:
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        return (f"HI, my name is {self.name},"
                f"I was born on {self.birth_date},"
                f" my profession is {self.occupation},"
                f" my highest education is {self.higher_education},")

person1 = Person("Tanay", "02-10-2009", "doctor", True )
person2 = Person("Atay", "26-10-2009", "singer", False)
person3 = Person("Sardar", "22-10-2009", "president", False)




print(person1.introduce())
print(person2.introduce())
print(person3.introduce())





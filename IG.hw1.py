class Person:
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education



    def introduce(self):
        if self.higher_education:
            higher_education = "I have higher education"
        else:
            higher_education = "I dont have higher education"
        return (f"HI, my name is {self.name},"
                f"I was born on {self.birth_date},"
                f" my profession is {self.occupation},"
                f" {higher_education},")


person1 = Person("Tanay", "2009-10-02", "doctor", True )
person2 = Person("Atay", "2009-10-26", "singer", False)
person3 = Person("Sardar", "2009-5-22", "president", False)

# person1.higher_education = False


print(person1.introduce())
print(person2.introduce())
print(person3.introduce())





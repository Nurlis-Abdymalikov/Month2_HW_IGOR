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

class Classmate(Person):
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool, group_name: str):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        return super().introduce() + f"group_name {self.group_name}"

class Friend(Person):
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool, hobby: str):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        return super().introduce() + f" Hobby {self.hobby}"

classmate1 = Classmate("Iskak", "2007-12-12", "policeman", True, "PhisMath")
classmate2 = Classmate("Mansur", "1997-10-3", "not", False, "economist")


friend1 = Friend("Nava","2008-1-2", "pilot", True, "volleyball")
friend2 = Friend("Macarov", "2010-2-13", "teacher", False, "football")

# print(classmate1.introduce())
# print(classmate2.introduce())
# print("--------------------------------------")
# print(friend1.introduce())
# print(friend2.introduce())


person = [classmate1, classmate2, friend1, friend2]

for i in person:
    print(i.introduce())


class BestFriend(Person):
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool, shared_memory: str):
        super().__init__(name, birth_date, occupation, higher_education)
        self.shared_memory = shared_memory

    def introduce(self):
        base_text = super().introduce()
        return base_text + f" You remember  {self.shared_memory}"


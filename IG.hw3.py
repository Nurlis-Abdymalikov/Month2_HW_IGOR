from datetime import datetime

class Person:
    def __init__(self, name: str, birth_date: str, occupation: str, higher_education: bool):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education


    @property
    def age(self):
        birthday = datetime.strptime(self.__birth_date, "%Y-%m-%d").date()
        now = datetime.today().date()

        age = now.year - birthday.year

        if (now.month, now.day) < (birthday.month, birthday.day):
            age -= 1
        return age



    def introduce(self):
        if self.__higher_education:
            higher_education = "I have higher education"
        else:
            higher_education = "I dont have higher education"
        return (f"HI, my name is {self.name},"
                f"I was born on {self.__birth_date},"
                f" my profession is {self.__occupation},"
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

classmate1 = Classmate("Iskak", "2007-12-12", "policeman", True, "10A")
classmate2 = Classmate("Mansur", "1997-10-3", "not", False, "11B")


friend1 = Friend("Nava","2008-1-2", "pilot", True, "volleyball")
friend2 = Friend("Macarov", "2010-2-13", "teacher", False, "football")


persons = [classmate1, classmate2, friend1, friend2]
for i in persons:
    print(i.introduce())

print(classmate1.age)

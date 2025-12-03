class Contact:
    def __init__(self, name, phone_number, id):
        self.name = name
        self.phone_number = phone_number
        self.id = id

    @staticmethod
    def validate_phone_number(phone_number):
        if len(str(phone_number)) != 10:
            return False
        return True

class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            ContactList.last_id += 1
            id = ContactList.last_id
            contact = Contact(name, phone_number, id)
            ContactList.all_contacts.append(contact)


    @classmethod
    def remove_contact(clc, id):
        for i in ContactList.all_contacts:
            if i.id == id:
                ContactList.all_contacts.remove(i)
                return
        print('id not found')


# пример использования
print(ContactList.last_id) # 0

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")
print(ContactList.last_id) # 2

ContactList.remove_contact(1)
ContactList.remove_contact(4)
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number, contact.id)
    # Виктор Цой 0500123456 2
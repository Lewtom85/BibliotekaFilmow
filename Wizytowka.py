from faker import Faker

fake = Faker()

class VisitCard:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def __repr__(self):
        return f"{self.name} {self.surname} - {self.email}"
    
    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.surname}, {self.position}, e-mail: {self.email}")

    @property
    def full_name_length(self):
        return len(self.name) + len(self.surname) + 1  # +1 for the space between names

class BaseContact(VisitCard):
    def __init__ (self, name, surname, email, phone):
        super().__init__(name, surname, email)
        self.phone = phone
    
    def contact(self):
        print(f"Wybieram numer prywatny {self.phone} i dzwonie do {self.name} {self.surname} ")
    
    @property
    def label_length(self):
        return  len(self.name) + len(self.surname) + 1 

class BusinessContact(VisitCard):
    def __init__(self, name, surname, email, company, position, phone):
        super().__init__(name, surname, email)
        self.company = company
        self.position = position
        self.phone = phone
    
    def contact(self):
        print(f"Wybieram numer slubowy {self.phone} i dzwonie do {self.name} {self.surname} ")
    
def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        name = fake.first_name()
        surname = fake.last_name()
        email = fake.email()
        phone = fake.phone_number()

        if contact_type == "base":
            contact = BaseContact(name, surname, email, phone)
        elif contact_type == "business":
            company = fake.company()
            position = fake.job()
            contact = BusinessContact(name, surname, email, company, position, phone)
        else:
            raise ValueError("Unknow cotact type")
        
        contacts.append(contact)
    return contacts

base_contacts = create_contacts("base", 3)
business_contacts = create_contacts("business", 3)

all_contacts = base_contacts + business_contacts

for contact in all_contacts:
    contact.contact()

by_name = sorted(all_contacts, key=lambda contact: contact.name)
by_surname = sorted(all_contacts, key=lambda contact: contact.surname)
by_email = sorted(all_contacts, key=lambda contact: contact.email)

print("Sortowanie według imienia:")
print(by_name)

print("Sortowanie według nazwiska:")
print(by_surname)

print("Sortowanie według adresu e-mail:")
print(by_email)

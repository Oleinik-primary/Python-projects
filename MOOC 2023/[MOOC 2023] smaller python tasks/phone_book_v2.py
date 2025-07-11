
# Write your solution here:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            new_person = Person(name)
            new_person.add_number(number)
            self.__persons[new_person.name()] = new_person
        else:
            self.__persons[name].add_number(number)
        

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        if name in self.__phonebook.all_entries():
            self.__phonebook.all_entries()[name].add_number(number)
        else:
            self.__phonebook.add_number(name, number)


    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if person == None:
            print("number unknown")
            print("address unknown")
        else:
            if person.numbers() == []:
                print("number unknown")  
            else:
                for number in person.numbers():
                    print(number)
            if person.address() == None:
                print("address unknown")
            else:  
                print(person.address()) 

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        person = self.__phonebook.get_entry(name)
        if person == None:
            new_person = Person(name)
            self.__phonebook.all_entries()[name] = new_person
            new_person.add_address(address)
        else:
            person.add_address(address)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = ""
    
    def name(self):
        return self.__name
    def numbers(self):
        return self.__numbers
    def address(self):
        if self.__address:
            return self.__address
        else:
            return None
        
    def add_number(self, num: str):
        self.__numbers.append(num)
    def add_address(self, address : str):
        self.__address = address
# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
# 1
# Erkki
# 02-123456
# 2
# Erkki
# 0


# task1
class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False


# task2
class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'City: {self.city}, ' \
               f'Street: {self.street}, ' \
               f'Zip code: {self.zip_code}, ' \
               f'Open hours {self.open_hours},' \
               f'Phone: {self.phone}'


class Book:
    def __init__(self,
                 library,
                 publication_date,
                 author_name,
                 author_surname,
                 number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Library: {self.library}, ' \
               f'Data publikacji {self.publication_date}, ' \
               f'Author name: {self.author_name} {self.author_surname},' \
               f'Number of pages: {self.number_of_pages}'


class Employee:
    def __init__(self,
                 first_name,
                 last_name,
                 hire_date,
                 birth_date,
                 city,
                 street,
                 zip_code,
                 phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Name and surname: {self.first_name} {self.last_name}, ' \
               f'Hire date: {self.hire_date}, ' \
               f'Birth date: {self.birth_date}, ' \
               f'City: {self.street}, ' \
               f'Zip code: {self.zip_code}, ' \
               f'Phone: {self.phone}'


class Order:
    def __init__(self,
                 employee: Employee,
                 student: Student,
                 books: Book,
                 order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Employee: {self.employee}, ' \
               f'Student: {self.student},' \
               f' Book: {self.books}, ' \
               f'Order date: {self.order_date}'


# task3

class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Area: {self.area}, Rooms: {self.rooms}, ' \
               f'Price: {self.price}, Address: {self.address}'


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Area: {self.area}, ' \
               f'Rooms: {self.rooms}, ' \
               f'Price: {self.price}, ' \
               f'Address: {self.address}, ' \
               f'Plot: {self.plot}'


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Area: {self.area}, ' \
               f'Rooms: {self.rooms}, ' \
               f'Price: {self.price}, ' \
               f'Address: {self.address}, ' \
               f'Floor: {self.floor}'


if __name__ == '__main__':
    # task1
    name_1 = 'Joanna Krawczyk'
    mark_1 = 100
    student_1 = Student(name_1, mark_1)
    print(student_1.is_passed())
    name_2 = 'Paweł Pawłowski'
    mark_2 = 35
    student_1 = Student(name_2, mark_2)
    print(student_1.is_passed())

    # task2
    lib1 = Library('Katowice', 'Katowicka', '11-111', '7:00 - 15:00',
                   '111 111 111')
    lib2 = Library('Gliwice', 'Gliwicka', '22-222', '8:00 - 16:00',
                   '222 222 222')

    ks1 = Book(lib1, '1990-02-02', 'Jan', 'Nowak', 301)
    ks2 = Book(lib2, '1991-10-01', 'Tadeusz', 'Kowalski', 302)
    ks3 = Book(lib1, '1992-01-03', 'Władysłąw', 'Mickiewicz', 303)
    ks4 = Book(lib2, '1993-03-04', 'Janina', 'Nowakowska', 304)
    ks5 = Book(lib1, '1994-04-05', 'Małgorzata', 'Płatek', 305)

    prac1 = Employee('Robert', 'Lewandowski', '2020-02-15', '1990-12-03',
                     'Katowice', 'Gdańska', '11-333',
                     '123 456 789')
    prac2 = Employee('Ewa', 'Kowalska', '2020-05-12', '1989-10-06',
                     'Gliwice', 'Cichociemnych', '11-100', '124 455 766')
    prac3 = Employee('Jan', 'Lewandowski', '2020-02-18', '1990-12-12',
                     'Katowice', 'Gdańska', '11-333', '111 444 777')

    stud1 = Student('Jan Student', 50)
    stud2 = Student('Paulina Student', 60)
    stud3 = Student('Piotr Student', 55)

    order1 = Order(prac1, stud1, ks1, '2021-10-25')
    order2 = Order(prac2, stud2, ks2, '2021-10-24')

    print(order1)
    print(order2)

    # task3
    house = House('area1', 6, 1000000, 'address1', 60)
    flat = Flat('area2', 3, 500000, 'address2', 1)
    print(house)
    print(flat)

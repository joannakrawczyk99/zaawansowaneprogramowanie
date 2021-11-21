import Book
import Employee
import Flat
import House
import Library
import Order
import Property
import Student

if __name__ == '__main__':
    # task1
    name_1 = 'Joanna Krawczyk'
    mark_1 = 100
    student_1 = Student.Student(name_1, mark_1)
    print(student_1.is_passed())
    name_2 = 'Paweł Pawłowski'
    mark_2 = 35
    student_1 = Student.Student(name_2, mark_2)

    print(student_1.is_passed())

    # task2
    lib1 = Library.Library('Katowice', 'Katowicka', '11-111', '7:00 - 15:00',
                   '111 111 111')
    lib2 = Library.Library('Gliwice', 'Gliwicka', '22-222', '8:00 - 16:00',
                   '222 222 222')

    ks1 = Book.Book(lib1, '1990-02-02', 'Jan', 'Nowak', 301)
    ks2 = Book.Book(lib2, '1991-10-01', 'Tadeusz', 'Kowalski', 302)
    ks3 = Book.Book(lib1, '1992-01-03', 'Władysłąw', 'Mickiewicz', 303)
    ks4 = Book.Book(lib2, '1993-03-04', 'Janina', 'Nowakowska', 304)
    ks5 = Book.Book(lib1, '1994-04-05', 'Małgorzata', 'Płatek', 305)

    prac1 = Employee.Employee('Robert', 'Lewandowski', '2020-02-15', '1990-12-03',
                     'Katowice', 'Gdańska', '11-333',
                     '123 456 789')
    prac2 = Employee.Employee('Ewa', 'Kowalska', '2020-05-12', '1989-10-06',
                     'Gliwice', 'Cichociemnych', '11-100', '124 455 766')
    prac3 = Employee.Employee('Jan', 'Lewandowski', '2020-02-18', '1990-12-12',
                     'Katowice', 'Gdańska', '11-333', '111 444 777')

    stud1 = Student.Student('Jan Student', 50)
    stud2 = Student.Student('Paulina Student', 60)
    stud3 = Student.Student('Piotr Student', 55)

    order1 = Order.Order(prac1, stud1, ks1, '2021-10-25')
    order2 = Order.Order(prac2, stud2, ks2, '2021-10-24')

    print(order1)
    print(order2)

    # task3
    house = House.House('area1', 6, 1000000, 'address1', 60)
    flat = Flat.Flat('area2', 3, 500000, 'address2', 1)
    print(house)
    print(flat)

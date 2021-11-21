import Book
import Employee
import Student


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

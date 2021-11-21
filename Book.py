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
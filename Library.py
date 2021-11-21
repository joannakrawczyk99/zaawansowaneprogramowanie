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

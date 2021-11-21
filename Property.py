class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'Area: {self.area}, ' \
               f'Rooms: {self.rooms}, ' \
               f'Price: {self.price}, ' \
               f'Address: {self.address}'

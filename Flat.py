import Property


class Flat(Property.Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Area: {self.area}, ' \
               f'Rooms: {self.rooms}, ' \
               f'Price: {self.price}, ' \
               f'Address: {self.address}, ' \
               f'Floor: {self.floor}'

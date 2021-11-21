import Property


class House(Property.Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Area: {self.area}, ' \
               f'Rooms: {self.rooms}, ' \
               f'Price: {self.price}, ' \
               f'Address: {self.address}, ' \
               f'Plot: {self.plot}'

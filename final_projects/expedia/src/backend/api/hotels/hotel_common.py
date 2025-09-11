from ..common.reservation import IReservation

class HotelRequest:
    def __init__(self, room_type, datetime_from, datetime_to, location, num_rooms, children, adults):
        self.room_type = room_type
        self.datetime_from = datetime_from
        self.datetime_to = datetime_to
        self.location = location
        self.num_rooms = num_rooms
        self.children = children
        self.adults = adults
        self.num_nights = (self.datetime_to - self.datetime_from).days
    
    def __repr__(self):
        return f'HiltonRequest: {self.room_type}, {self.datetime_from}, \
        {self.datetime_to}, {self.location}, {self.num_rooms}, {self.children}, {self.adults}, {self.num_nights}'

class Hotel:
    def __init__(self, hotel_name, price_per_night, request: HotelRequest, hotel_mgr):
        self.hotel_name = hotel_name
        self.price_per_night = price_per_night
        self.request = request
        self.hotel_mgr = hotel_mgr
    
    @property
    def total_cost(self):
        return self.price_per_night * self.request.num_nights * self.request.num_rooms
    
    def __repr__(self):
        return f'Hotel: {self.hotel_name}, Price per night: {self.price_per_night}, \
        Total Cost: {self.total_cost}, Request: ({self.request})'

class HotelReservation(IReservation):
    def __init__(self, hotel: Hotel, customers_info: list):
        super().__init__()
        self.hotel = hotel
        self.customers_info = customers_info
    
    @property
    def total_cost(self):
        return self.hotel.total_cost
    
    @property
    def mgr(self):
        return self.hotel.hotel_mgr
    
    def __repr__(self):
        return repr(self.hotel)
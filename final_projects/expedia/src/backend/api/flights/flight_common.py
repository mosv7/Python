from ..common.reservation import IReservation

class FlightRequest:
    def __init__(self, datetime_from, from_loc, datetime_to, to_loc, infants, adults, children):
        self.datetime_from = datetime_from
        self.from_loc = from_loc
        self.datetime_to = datetime_to
        self.to_loc = to_loc
        self.infants = infants
        self.adults = adults
        self.children = children
    
    def __repr__(self):
        return f'Flight Request from {self.from_loc} to {self.to_loc} on {self.datetime_from} - {self.datetime_to}, ' + \
            f'Infants: {self.infants}, Adults: {self.adults}, Children: {self.children}'

class Flight:
    def __init__(self, airline_name, total_cost, request: FlightRequest, flight_mgr):
        self.airline_name = airline_name
        self.total_cost = total_cost
        self.request = request
        self.flight_mgr = flight_mgr

    def __repr__(self):
        return f'Flight with {self.airline_name}, Total Cost: {self.total_cost}, ' + \
            f'Request: ({self.request})'

class FlightReservation(IReservation):
    def __init__(self, flight: Flight, customers_info: list):
        super().__init__()
        self.flight = flight
        self.customers_info = customers_info
    
    @property
    def total_cost(self):
        return self.flight.total_cost
    
    @property
    def mgr(self):
        return self.flight.flight_mgr
    
    def __repr__(self):
        return repr(self.flight)
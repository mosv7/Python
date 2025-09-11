class Turkish_CustomerInfo:
    def __init__(self, passport, name, birthdate):
        pass

class TurkishFlight:
    def __init__(self, cost, date_time_from, date_time_to):
        self.cost = cost
        self.date_time_from = date_time_from
        self.date_time_to = date_time_to

class TurkishOnlineAPI:
    def set_from_to_info(self, date_time_from, from_loc, date_time_to, to_loc):
        pass

    def set_passenger_info(self, infants, children, adults):
        pass

    def get_available_flights(self):
        flights = []
        flights.append(TurkishFlight(300, "25-01-2022", "10-02-2022"))
        flights.append(TurkishFlight(350, "29-01-2022", "10-02-2022"))
        return flights
    
    @staticmethod
    def reserve_flight(customers_info: list, flight: TurkishFlight):
        confirmation_id = '1234TTTTT'  # None for failure
        return confirmation_id

    @staticmethod
    def cancel_flight(confirmation_id):
        return True
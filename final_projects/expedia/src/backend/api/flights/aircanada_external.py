class AirCanadaCustomerInfo:
    def __init__(self, name, passport, birthdate):
        pass

class AirCanadaFlight:
    def __init__(self, price, date_time_from, date_time_to):
        self.price = price
        self.date_time_from = date_time_from
        self.date_time_to = date_time_to

class AirCandaOnlineAPI:
    @staticmethod
    def get_flights(from_loc, from_date, to_loc, to_date, adults, children):
        flights = []
        flights.append(AirCanadaFlight(200, "25-01-2022", "10-02-2022"))
        flights.append(AirCanadaFlight(250, "29-01-2022", "10-02-2022"))
        return flights
    
    @staticmethod
    def reserve_flight(flight: AirCanadaFlight, customers_info: list):
        confirmation_id = '1234AirCanadaXXr34'  # None for failure
        return confirmation_id
    
    @staticmethod
    def cancel_flight(confirmation_id):
        return True
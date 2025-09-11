from .flight_common import FlightRequest, Flight, FlightReservation
from .turkish_external import TurkishOnlineAPI, Turkish_CustomerInfo, TurkishFlight
from ..common.customer_info import CustomerInfo
from ..common.reservation import IReservationManager

class TurkishFlightManager(IReservationManager):
    def __init__(self):
        self.api = TurkishOnlineAPI()
    
    def search(self, request: FlightRequest):
        self.api.set_from_to_info(
            date_time_from=request.datetime_from,
            from_loc=request.from_loc,
            date_time_to=request.datetime_to,
            to_loc=request.to_loc
        )

        self.api.set_passenger_info(
            infants=request.infants,
            children=request.children,
            adults=request.adults
        )

        flights_external = self.api.get_available_flights()

        flights = []
        for flight in flights_external:
            flights.append(Flight(
                airline_name='Turkish Airlines',
                total_cost=flight.cost,
                request=request,
                flight_mgr=self
            ))
        return flights
    
    @staticmethod
    def _to_turkish_customer_info_external(customers_info: list):
        result = []
        for customer_info in customers_info:
            result.append(Turkish_CustomerInfo(
                passport=customer_info.passport,
                name=customer_info.name,
                birthdate=customer_info.birthdate
            ))
        return result
    
    @staticmethod
    def _to_turkish_flight_external(flight: Flight):
        return TurkishFlight(
            cost=flight.total_cost,
            date_time_from=flight.request.datetime_from,
            date_time_to=flight.request.datetime_to
        )
    
    def reserve(self, reservation: FlightReservation):
        flight = self._to_turkish_flight_external(reservation.flight)
        customers_info = self._to_turkish_customer_info_external(reservation.customers_info)
        return TurkishOnlineAPI.reserve_flight(customers_info, flight)
    
    def cancel(self, reservation: FlightReservation):
        return TurkishOnlineAPI.cancel_flight(reservation.confirmation_id)
from .flight_common import FlightRequest, Flight, FlightReservation
from .aircanada_external import AirCandaOnlineAPI, AirCanadaCustomerInfo, AirCanadaFlight
from ..common.customer_info import CustomerInfo
from ..common.reservation import IReservationManager


class AirCanadaFlightManager(IReservationManager):
    def __init__(self):
        pass

    def search(self, request: FlightRequest):
        flight_external = AirCandaOnlineAPI.get_flights(
            from_loc=request.from_loc,
            from_date=request.datetime_from,
            to_loc=request.to_loc,
            to_date=request.datetime_to,
            adults=request.adults,
            children=request.children
        )

        flights = []
        for flight in flight_external:
            flights.append(Flight(
                airline_name='AirCanada',
                total_cost=flight.price,
                request=request,
                flight_mgr=self
            ))
        return flights
    
    def reserve(self, reservation: FlightReservation):
        flight = self._to_aircanada_flight_external(reservation.flight)
        customers_info = self._to_aircanada_customer_info_external(reservation.customers_info)
        return AirCandaOnlineAPI.reserve_flight(flight, customers_info)
    
    def cancel(self, reservation):
        return AirCandaOnlineAPI.cancel_flight(reservation.confirmation_id)
    
    @staticmethod
    def _to_aircanada_flight_external(flight: Flight):
        return AirCanadaFlight(
            price=flight.total_cost,
            date_time_from=flight.request.datetime_from,
            date_time_to=flight.request.datetime_to
        )
    
    @staticmethod
    def _to_aircanada_customer_info_external(customers_info: list):
        external_customers_info = []
        for customer_info in customers_info:
            external_customers_info.append(AirCanadaCustomerInfo(
                name=customer_info.name,
                passport=customer_info.passport,
                birthdate=customer_info.birthdate
            ))
        return external_customers_info
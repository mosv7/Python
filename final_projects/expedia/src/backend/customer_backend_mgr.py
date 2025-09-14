from .api.flights.flights_mgr import FlightsManager
from .api.flights.flight_common import FlightRequest
from .api.hotels.hotels_mgr import HotelsManager
from .api.hotels.hotel_common import HotelRequest
from .api.common.reservation import ItineraryReservation, IReservation
from .api.payment.paypal_payment import PaypalPayment
from .common.exceptions import ExpediaPaymentException, ExpediaReservationException

class CustomerBackendManager:
    def __init__(self, customer):
        self.customer = customer
        self.flights_manager = FlightsManager()
        self.hotels_manager = HotelsManager()
        self.payment_processor = PaypalPayment()

    def search_flights(self, flight_request: FlightRequest):
        return self.flights_manager.search(flight_request)
    
    def search_hotels(self, hotel_request: HotelRequest):
        return self.hotels_manager.search(hotel_request)
    
    def get_payment_choices(self):
        return [repr(card) for card in self.customer.payment_cards]
    
    def _make_payment(self, cost, card):
        self.payment_processor.set_user_info(card.owener_name, card.address)
        self.payment_processor.set_card_info(card.number, card.expiry, card.cvv)
        status, transaction_id = self.payment_processor.make_payment(cost)
        return status, transaction_id
    
    def _cancel_payment(self, transaction_id):
        return self.payment_processor.cancel_payment(transaction_id)
    
    def _cancel_reservation(self, reservations):
        for reservation in reservations:
            reservation.mgr.cancel(reservation)
    
    def _reserve(self, reservations):
        if not isinstance(reservations, list):
            reservations = [reservations]
        
        reserved_items = []
        for reservation in reservations:
            confirmation_id = reservation.mgr.reserve(reservation)
            if confirmation_id:
                reservation.confirmation_id = confirmation_id
                reserved_items.append(reservation)
            else:
                reservation.mgr.cancel(reserved_items)
                return False
        return True
    
    def pay_and_reserve(self, reservation: IReservation, card_idx):
        payment_card = self.customer.payment_cards[card_idx]
        total_cost = reservation.total_cost
        is_paid, transaction_id = self._make_payment(total_cost, payment_card)

        if is_paid:
            if isinstance(reservation, ItineraryReservation):
                is_reserved = self._reserve(reservation.reservations)
            else:
                is_reserved = self._reserve(reservation)

            if not is_reserved:
                self._cancel_payment(transaction_id)
                raise ExpediaReservationException
        
        else:
            raise ExpediaPaymentException


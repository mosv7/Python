from .hotel_common import HotelRequest, Hotel, HotelReservation
from .marriott_external import MarriottHotelAPI, MarriottCustomerInfo, MarriottRoom
from ..common.reservation import IReservationManager
from ..common.customer_info import CustomerInfo

class MarriottHotelManager(IReservationManager):
    def search(self, request: HotelRequest):
        hotel_externals = MarriottHotelAPI.search_available_rooms(
            location=request.location,
            from_date=request.datetime_from,
            to_date=request.datetime_to,
            adults=request.adults,
            children=request.children,
            neededrooms=request.num_rooms
        )

        hotels = []
        for hotel_external in hotel_externals:
            hotels.append(Hotel("Marriott", hotel_external.price_per_night, request, self))
        return hotels
    
    def reserve(self, reservation: HotelReservation):
        pass

    @staticmethod
    def _to_marriott_hotel_external(hotel: Hotel):
        return MarriottRoom(
            hotel.request.room_type,
            hotel.request.num_rooms,
            hotel.price_per_night,
            hotel.request.datetime_from,
            hotel.request.datetime_to
        )
    
    @staticmethod
    def _to_marriott_customer_info(customers_info: list):
        result = []
        for customer in customers_info:
            customer: CustomerInfo = customer
            result.append(MarriottCustomerInfo(customer.name, customer.passport, customer.birthdate))
        
        return result
    
    def cancel(self, reservation):
        return MarriottHotelAPI.cancel_room(reservation.confirmation_id)
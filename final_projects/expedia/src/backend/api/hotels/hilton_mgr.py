from .hotel_common import HotelRequest, Hotel, HotelReservation
from .hilton_external import HiltonHotelAPI, HiltonCustomerInfo, HiltonRoom
from ..common.reservation import IReservationManager
from ..common.customer_info import CustomerInfo

class HiltonHotelManager(IReservationManager):
    def search(self, request: HotelRequest):
        hotels_external = HiltonHotelAPI.search_rooms(
            location=request.location,
            from_date=request.datetime_from,
            to_date=request.datetime_to,
            num_rooms=request.num_rooms,
            adults=request.adults,
            children=request.children
        )
    
        hotels = []
        for hotel_external in hotels_external:
            hotels.append(Hotel("Hilton", hotel_external.price_per_night, request, self))
        return hotels
    
    def reserve(self, reservation: HotelReservation):
        hotel = self._to_hilton_hotel_external(reservation.hotel)
        customers_Info = self._to_hilton_customer_info(reservation.customers_info)
        return HiltonHotelAPI.reserve_room(hotel, customers_Info)

    def cancel(self, reservation):
        return HiltonHotelAPI.cancel_room(reservation.confirmation_id)

    @staticmethod
    def _to_hilton_hotel_external(hotel: Hotel):
        return HiltonRoom(
            hotel.request.room_type,
            hotel.request.num_rooms,
            hotel.price_per_night,
            hotel.request.datetime_from,
            hotel.request.datetime_to
        )

    @staticmethod
    def _to_hilton_customer_info(customers_info: list):
        result = []
        for customer in customers_info:
            customer: CustomerInfo = customer
            result.append(HiltonCustomerInfo(customer.name, customer.passport, customer.birthdate))
        
        return result


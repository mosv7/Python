from ..common.reservation import ReservationManagersProcessor
from .hilton_mgr import HiltonHotelManager
from .marriott_mgr import MarriottHotelManager


class HotelsManager(ReservationManagersProcessor):
    def __init__(self):
        super().__init__([HiltonHotelManager(), MarriottHotelManager()])
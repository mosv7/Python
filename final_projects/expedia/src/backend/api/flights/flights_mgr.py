from ..common.reservation import ReservationManagersProcessor
from .aircanada_mgr import AirCanadaFlightManager
from .turkish_mgr import TurkishFlightManager

class FlightsManager(ReservationManagersProcessor):
    def __init__(self):
        super().__init__([
            AirCanadaFlightManager(),
            TurkishFlightManager()
        ])
class ExpediaException(BaseException):
    """Base class for all exceptions in the Expedia project."""
    pass

class ExpediaPaymentException(ExpediaException):
    """Base class for all payment-related exceptions in the Expedia project."""
    pass

class ExpediaReservationException(ExpediaException):
    """Base class for all reservation-related exceptions in the Expedia project."""
    pass
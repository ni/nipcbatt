class LimitException(BaseException):
    def __init__(
        self,
        called_class: str,
        called_method: str,
        test: str,
        lower_limit: float,
        upper_limit: float,
        unit: str,
        value: float,
    ) -> None:
        self.caller = "Sequence : " + called_class + ", method : " + called_method
        self.message = (
            test
            + " should be between "
            + str(lower_limit)
            + " and "
            + str(upper_limit)
            + unit
            + ", Result "
            + str(value)
        )

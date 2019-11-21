from datetime import datetime
from datetime import timedelta


class CountDown:
    """
    count down:
        1: save in database in table campaing a dateEnd
        2: enabled a dateEnd when campaing is public
    """

    def __init__(self):
        pass

    @classmethod
    def campaingEnd(cls, data):
        """
        sum public_at qty_days
        return total_days
        if we need to add minutes
        timedelta(days=1,minutes=5)
        """
        total_days = data.public_at + timedelta(days=data.qty_days)
        return total_days

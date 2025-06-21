from rest_framework import throttling
import datetime
from rest_framework.exceptions import Throttled

class CustomThrottle(throttling.BaseThrottle):
    def allow_request(self, request, veiw):
        now = datetime.datetime.now().hour
        if now >= 23 and now <= 0:
             raise Throttled(detail='Bro dont spam! We are in a lunch break.')
        return True
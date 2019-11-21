from django.dispatch import Signal, receiver
from .models import Campaing
from tools import CountDown


ping_signal = Signal(providing_args=["context"])


class SignalDemo:
    def ping(self):
        print('PING')
        ping_signal.send(sender=self.__class__, PING=True)


@receiver(ping_signal)
def pong(**kwargs):
    if kwargs['PING']:
        print('PONG')


demo = SignalDemo()
demo.ping()

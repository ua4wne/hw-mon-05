import logging
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import random

sentry_sdk.init(
    dsn="YOUR DSN HERE",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)
sentry_logging = LoggingIntegration(level=logging.INFO, event_level=logging.ERROR)


class DigitException(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"Недопустимое значение: {self.num}. " \
               f"Значение числа не должно быть равным 5!!!"


def check_rules():
    while True:
        attempt = random.randint(1, 6)
        if attempt in [1, 3]:
            result = attempt / 0
        if attempt == 5:
            raise DigitException(5)


if __name__ == "__main__":
    check_rules()

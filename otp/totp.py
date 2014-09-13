"""Implementation of RFC 6238 TOTP.

http://tools.ietf.org/html/rfc6238
"""

import logging
import time
import math
from otp import Otp

TIME_STEP = 30000  # msec
DIGIT = 6

_logger = logging.getLogger(__name__)


class Totp(Otp):
    def __init__(self, secret, initial_time=0, algorithm='SHA1', digit=DIGIT):
        super().__init__(secret, algorithm, digit)
        self._initial_time = initial_time

    def get_next_count(self):
        elapsed = math.floor(time.time() * 1000) - self._initial_time
        return math.floor(elapsed / TIME_STEP)


def main():
    logging.basicConfig(level=logging.INFO)

    secret = b'Hello!\xde\xad\xbe\xef'
    # otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example
    otp = Totp(secret)
    while True:
        print(otp.get_otp())
        time.sleep(1)

if __name__ == '__main__':
    main()

"""Implementation of RFC 4226 HOTP.

http://tools.ietf.org/html/rfc4226
"""

import logging
from otp import Otp

DIGIT = 6

_logger = logging.getLogger(__name__)


class Hotp(Otp):
    def __init__(self, secret, counter=0, algorithm='SHA1', digit=DIGIT):
        super().__init__(secret, algorithm, digit)
        self._counter = counter

    def get_next_count(self):
        last = self._counter
        self._counter += 1
        return last


def main():
    logging.basicConfig(level=logging.INFO)

    secret = b'Hello!\xde\xad\xbe\xef'
    counter = 1
    # Expected OTPs were obtained by Google Authenticator
    # with URI otpauth://hotp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&counter=1&issuer=Example
    expected_otps = [
        996554, 602287, 143627, 960129, 768897,
        883951, 449891, 964230, 924769, 930313
    ]

    hotp = Hotp(secret, counter)
    for i in range(0, len(expected_otps)):
        otp = hotp.get_otp()
        logging.info('otp[{:02}]: {} == {:06}'.format(i, otp, expected_otps[i]))
        assert otp == str(expected_otps[i])


if __name__ == '__main__':
    main()

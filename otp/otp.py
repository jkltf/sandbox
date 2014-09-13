"""Common codes for Generating H/TOTPs.
"""

import struct
import logging
import hmac

_logger = logging.getLogger(__name__)


class Otp:
    def __init__(self, secret, algorithm='SHA1', digit=6):
        self._secret = secret
        self._algorithm = algorithm
        self._digit = digit
        self._otp_format = '{{:0{}}}'.format(digit)

    def get_otp(self):
        counter = self.get_next_count()
        hs = hmac.new(self._secret, struct.pack('!Q', counter), self._algorithm).digest()
        _logger.debug('hmac: {}, {}'.format(hs, len(hs)))
        sbits = self.__do_dynamic_truncation(hs)
        otp = sbits % 10 ** self._digit
        return self._otp_format.format(otp)

    def __get_next_count(self):
        pass

    @staticmethod
    def __do_dynamic_truncation(hmac_sha1):
        offset = int.from_bytes(hmac_sha1, byteorder='big') & 0x0F
        _logger.debug('hmac_sha1[-1]: b{:b}, offset: b{:b}, offset: {}'.format(hmac_sha1[-1], offset, offset))

        p = (hmac_sha1[offset] & 0x7F) << 24
        p |= (hmac_sha1[offset + 1] & 0xFF) << 16
        p |= (hmac_sha1[offset + 2] & 0xFF) << 8
        p |= hmac_sha1[offset + 3] & 0xFF
        return p


from Crypto.Util.strxor import strxor_c
from Crypto.Util.strxor import strxor
from Crypto.Random import random
from Crypto.Util.strxor import strxor

import binascii
import BaseHTTPServer
import SocketServer
import time
import urlparse 


def to_bytes(n, length, endianess='big'):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if endianess == 'big' else s[::-1]

def randbytes(k):
    return to_bytes(random.getrandbits(8*k), k)

PORT = 9000
DELAY = 0.05

blocksize = 64
key = randbytes(100)

# Taken from https://github.com/sfstpala/SlowSHA
class SHA1 (object):
    _default_h0, _default_h1, _default_h2, _default_h3, _default_h4, = (
        0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476, 0xc3d2e1f0)

    def __init__(self, message, h0 = _default_h0, h1 = _default_h1, h2 = _default_h2, h3 = _default_h3, h4 = _default_h4, length = None):
        self._h0 = h0
        self._h1 = h1
        self._h2 = h2
        self._h3 = h3
        self._h4 = h4
        if length is None:
            length = len(message) * 8
        length = bin(length)[2:].rjust(64, "0")
        while len(message) > 64:
            self._handle(''.join(bin(ord(i))[2:].rjust(8, "0") for i in message[:64]))
            message = message[64:]
        message = ''.join(bin(ord(i))[2:].rjust(8, "0") for i in message) + "1"
        message += "0" * ((448 - len(message) % 512) % 512) + length
        for i in range(len(message) // 512):
            self._handle(message[i * 512:i * 512 + 512])


    def _handle(self, chunk):

        lrot = lambda x, n: (x << n) | (x >> (32 - n))
        w = []

        for j in range(len(chunk) // 32):
            w.append(int(chunk[j * 32:j * 32 + 32], 2))

        for i in range(16, 80):
            w.append(lrot(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1)
                & 0xffffffff)

        a = self._h0
        b = self._h1
        c = self._h2
        d = self._h3
        e = self._h4
        for i in range(80):

            if i <= i <= 19:
                f, k = d ^ (b & (c ^ d)), 0x5a827999
            elif 20 <= i <= 39:
                f, k = b ^ c ^ d, 0x6ed9eba1
            elif 40 <= i <= 59:
                f, k = (b & c) | (d & (b | c)), 0x8f1bbcdc
            elif 60 <= i <= 79:
                f, k = b ^ c ^ d, 0xca62c1d6
                
            temp = lrot(a, 5) + f + e + k + w[i] & 0xffffffff
            a, b, c, d, e = temp, a, lrot(b, 30), c, d

        self._h0 = (self._h0 + a) & 0xffffffff
        self._h1 = (self._h1 + b) & 0xffffffff
        self._h2 = (self._h2 + c) & 0xffffffff
        self._h3 = (self._h3 + d) & 0xffffffff
        self._h4 = (self._h4 + e) & 0xffffffff

    def _digest(self):
        return (self._h0, self._h1, self._h2, self._h3, self._h4)

    def hexdigest(self):
        return ''.join(hex(i)[2:].rjust(8, "0")
            for i in self._digest())

    def digest(self):
        hexdigest = self.hexdigest()
        return bytearray(int(hexdigest[i * 2:i * 2 + 2], 16) for i in range(len(hexdigest) // 2))
        
def authSHA1(key, message):
    return SHA1(key + message).digest()

def sha1(x):
    return SHA1(x).digest()

def hmacSHA1(key, message):
    if len(key) > blocksize:
        key = sha1(key)
    if len(key) < blocksize:
        key += b'\x00' * (blocksize - len(key))

    opad = strxor_c(key, 0x5c)
    ipad = strxor_c(key, 0x36)

    return sha1(opad + sha1(ipad + message))

def insecure_compare(x, y):
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        if x[i] != y[i]:
            return False
        time.sleep(DELAY)
    return True

last_file = b''

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global last_file
        result = urllib.parse.urlparse(self.path)
        if result.path == '/test':
            q = urllib.parse.parse_qs(result.query)
            file = q['file'][0].encode('ascii')
            digest = hmacSHA1(key, file)
            signature = binascii.unhexlify(q['signature'][0])
            if file != last_file:
                last_file = file
                print('New file:', file, binascii.hexlify(digest))
            print(binascii.hexlify(digest), binascii.hexlify(signature))
            if insecure_compare(digest, signature):
                self.send_error(200)
            else:
                self.send_error(500)
        else:
            self.send_error(500)

def serve_forever(delay):
    global DELAY
    DELAY = delay
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("", PORT), RequestHandler)
    print("serving at port {0} with delay {1}".format(PORT, DELAY))
    httpd.serve_forever()

if __name__ == '__main__':
    serve_forever(DELAY)
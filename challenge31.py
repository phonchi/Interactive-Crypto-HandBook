
import binascii
import sys
import time
import urllib2


def isValidSignature(file, signature):
    start =time.time()
    try:
        response = urllib2.urlopen('http://localhost:9000/test?file=' + file + '&signature=' + signature)
        end = time.time()
        if response.status != 200:
            raise Exception('unexpected status ' + str(response.status))
        return (True, end - start)
    except urllib2.HTTPError as e:
        end = time.time()
        if e.code != 500:
            raise
        return (False, end - start)

def guessNextByte(file, knownBytes, delay):
    suffixlen = 20 - len(knownBytes)
    expectedDuration = delay * len(knownBytes) + 0.01
    start = time.time()

    def print_info(i):
        end = time.time()
        print('Made {0} requests in {1:.2f}s; rps = {2:.2f}, max rps = {3:.2f}'.format(i, end - start, i / (end - start), 1 / expectedDuration))

    for i in range(256):
        suffix = bytes([i]) + (b'\x00' * (suffixlen - 1))
        signature = knownBytes + suffix
        _, duration = isValidSignature(file, binascii.hexlify(signature).decode('ascii'))
        if duration > expectedDuration + 0.8 * delay:
            print_info(i)
            return knownBytes + bytes([i])

    raise Exception('unexpected')

if __name__ == '__main__':
    file = sys.argv[1]
    knownBytes = b''
    DELAY = 0.05
    for i in range(20):
        knownBytes = guessNextByte(file, knownBytes, DELAY)
        print(binascii.hexlify(knownBytes))
    print(binascii.hexlify(knownBytes))
    if not isValidSignature(file, binascii.hexlify(knownBytes).decode('ascii'))[0]:
        raise Exception('unexpected')
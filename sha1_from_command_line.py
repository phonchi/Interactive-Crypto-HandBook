#!/usr/bin/env python

##  sha1_from_command_line.py
##  by Avi Kak (kak@purdue.edu)
##  February 19, 2013
##  Modified: March 2, 2016

## Call syntax:
##
##     sha1_from_command_line.py   your_message_string

##  This script takes its message on the standard input from
##  the command line and sends the hash to its standard
##  output.  NOTE: IT ADDS A NESWLINE AT THE END OF THE OUTPUT
##  TO SHOW THE HASHCODE IN A LINE BY ITSELF.

import sys
import BitVector
if BitVector.__version__ < '3.2':
    sys.exit("You need BitVector module of version 3.2 or higher" )
from BitVector import *

if len(sys.argv) != 2:
    sys.stderr.write("Usage: %s  <string to be hashed>\n" % sys.argv[0])
    sys.exit(1)

message = sys.argv[1]

# Initialize hashcode for the first block. Subsequetnly, the
# output for each 512-bit block of the input message becomes
# the hashcode for the next block of the message.
h0 = BitVector(hexstring='67452301')
h1 = BitVector(hexstring='efcdab89')
h2 = BitVector(hexstring='98badcfe')
h3 = BitVector(hexstring='10325476')
h4 = BitVector(hexstring='c3d2e1f0')

bv = BitVector(textstring = message)
length = bv.length()
bv1 = bv + BitVector(bitstring="1")
length1 = bv1.length()
howmanyzeros = (448 - length1) % 512
zerolist = [0] * howmanyzeros
bv2 = bv1 + BitVector(bitlist = zerolist)
bv3 = BitVector(intVal = length, size = 64)
bv4 = bv2 + bv3

words = [None] * 80

for n in range(0,bv4.length(),512):
    block = bv4[n:n+512]
    words[0:16] = [block[i:i+32] for i in range(0,512,32)]
    for i in range(16, 80):
        words[i] = words[i-3] ^ words[i-8] ^ words[i-14] ^ words[i-16]
        words[i] << 1
        a,b,c,d,e = h0,h1,h2,h3,h4
    for i in range(80):
        if (0 <= i <= 19):
            f = (b & c) ^ ((~b) & d)
            k = 0x5a827999
        elif (20 <= i <= 39):
            f = b ^ c ^ d
            k = 0x6ed9eba1
        elif (40 <= i <= 59):
            f = (b & c) ^ (b & d) ^ (c & d) 
            k = 0x8f1bbcdc
        elif (60 <= i <= 79):
            f = b ^ c ^ d
            k = 0xca62c1d6
        a_copy = a.deep_copy()
        T = BitVector( intVal = (int(a_copy << 5) + int(f) + int(e) + int(k) + \
                                              int(words[i])) & 0xFFFFFFFF, size=32 )
        e = d
        d = c
        b_copy = b.deep_copy()
        b_copy << 30
        c = b_copy
        b = a
        a = T
    h0 = BitVector( intVal = (int(h0) + int(a)) & 0xFFFFFFFF, size=32 )
    h1 = BitVector( intVal = (int(h1) + int(b)) & 0xFFFFFFFF, size=32 )
    h2 = BitVector( intVal = (int(h2) + int(c)) & 0xFFFFFFFF, size=32 )
    h3 = BitVector( intVal = (int(h3) + int(d)) & 0xFFFFFFFF, size=32 )
    h4 = BitVector( intVal = (int(h4) + int(e)) & 0xFFFFFFFF, size=32 )

message_hash = h0 + h1 + h2 + h3 + h4
hash_hex_string = message_hash.getHexStringFromBitVector()
sys.stdout.writelines((hash_hex_string, "\n"))

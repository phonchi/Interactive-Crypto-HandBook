#!/usr/bin/env python

from BitVector import *

# Construct an EMPTY bit vector (a bit vector of size 0):
print("\nConstructing an EMPTY bit vector (a bit vector of size 0):")
bv1 = BitVector( size = 0 )
print(bv1)                                   # no output

# Construct a bit vector of size 2:
print("\nConstructing a bit vector of size 2:")
bv2 = BitVector( size = 2 )
print(bv2)                                   # 00

# Joining two bit vectors:
print("\nConcatenating two previously constructed bit vectors:")
result = bv1 + bv2
print(result)                                # 00

# Construct a bit vector with a tuple of bits:
print("\nConstructing a bit vector from a tuple of bits:")
bv = BitVector(bitlist=(1, 0, 0, 1))
print(bv)                                    # 1001

# Construct a bit vector with a list of bits:    
print("\nConstructing a bit vector from a list of bits:")
bv = BitVector(bitlist=[1, 1, 0, 1])
print(bv)                                    # 1101

# Construct a bit vector from an integer
bv = BitVector(intVal=5678)
print("\nBit vector constructed from integer 5678:")
print(bv)                                    # 1011000101110
print("\nBit vector constructed from integer 0:")
bv = BitVector(intVal=0)
print(bv)                                    # 0
print("\nBit vector constructed from integer 2:")
bv = BitVector(intVal=2)
print(bv)                                    # 10
print("\nBit vector constructed from integer 3:")
bv = BitVector(intVal=3)
print(bv)                                    # 11
print("\nBit vector constructed from integer 123456:")
bv = BitVector(intVal=123456)
print(bv)                                    # 11110001001000000
print("\nInt value of the previous bit vector as computed by intVal():")
print(bv.intValue())                         # 123456
print("\nInt value of the previous bit vector as computed by int():")
print(int(bv))                               # 123456

# Construct a bit vector from a very large integer:
x = 12345678901234567890123456789012345678901234567890123456789012345678901234567890
bv = BitVector(intVal=x)
print("\nHere is a bit vector constructed from a very large integer:")
print(bv)
print("The integer value of the above bit vector is:%d" % int(bv))

# Construct a bit vector directly from a file-like object:
import io
x = "111100001111"
x = ""
if sys.version_info[0] == 3:    
    x = "111100001111"
else:                           
    x = unicode("111100001111")
fp_read = io.StringIO(x)
bv = BitVector( fp = fp_read )
print("\nBit vector constructed directed from a file like object:")
print(bv)                                    # 111100001111 

# Construct a bit vector directly from a bit string:
bv = BitVector( bitstring = '00110011' )
print("\nBit Vector constructed directly from a bit string:")
print(bv)                                    # 00110011

bv = BitVector(bitstring = '')
print("\nBit Vector constructed directly from an empty bit string:")
print(bv)                                    # nothing
print("\nInteger value of the previous bit vector:")
print(bv.intValue())                         # 0

# Construct a bit vector from a text string:
print("\nConstructing a bit vector from the textstring 'hello':")
bv3 = BitVector(textstring = "hello")
print(bv3)                # 0110100001100101011011000110110001101111
mytext = bv3.get_bitvector_in_ascii()
print("Text recovered from the previous bitvector: ")
print(mytext)                                         # hello
print("\nConstructing a bit vector from the textstring 'hello\\njello':")
bv3 = BitVector(textstring = "hello\njello")
print(bv3)   # 0110100001100101011011000110110001101111000010100110101001100101011011000110110001101111
mytext = bv3.get_bitvector_in_ascii()
print("Text recovered from the previous bitvector:")
print(mytext)                                         # hello
                                                      # jello
# Construct a bit vector from a hex string:                                                      
print("\nConstructing a bit vector from the hexstring '68656c6c6f':")
bv4 = BitVector(hexstring = "68656c6c6f")
print(bv4)                # 0110100001100101011011000110110001101111
myhexstring = bv4.get_bitvector_in_hex()
print("Hex string recovered from the previous bitvector: ")
print(myhexstring)                                    # 68656c6c6f

print("\nConstructing a bit vector from the uppercase hexstring '68656C6C6F':")
bv4 = BitVector(hexstring = "68656C6C6F")
print(bv4)                # 0110100001100101011011000110110001101111
myhexstring = bv4.get_bitvector_in_hex()
print("Hex string recovered from the previous bitvector: ")
print(myhexstring)                                    # 68656c6c6f

# Construct a bit vector from a string of raw bytes:
print("\nDemonstrating the raw bytes mode of constructing a bit vector (useful for reading public and private keys):")
mypubkey = 'ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA5amriY96HQS8Y/nKc8zu3zOylvpOn3vzMmWwrtyDy+aBvns4UC1RXoaD9rDKqNNMCBAQwWDsYwCAFsrBzbxRQONHePX8lRWgM87MseWGlu6WPzWGiJMclTAO9CTknplG9wlNzLQBj3dP1M895iLF6jvJ7GR+V3CRU6UUbMmRvgPcsfv6ec9RRPm/B8ftUuQICL0jt4tKdPG45PBJUylHs71FuE9FJNp01hrj1EMFObNTcsy9zuis0YPyzArTYSOUsGglleExAQYi7iLh17pAa+y6fZrGLsptgqryuftN9Q4NqPuTiFjlqRowCDU7sSxKDgU7bzhshyVx3+pzXO4D2Q== kak@pixie'
import base64
if sys.version_info[0] == 3:    
    import binascii
    keydata = base64.b64decode(bytes(mypubkey.split(None)[1], 'utf-8'))
else:
    keydata = base64.b64decode(mypubkey.split(None)[1])
bv = BitVector( rawbytes = keydata )
print(bv)

# Test array-like indexing for a bit vector:
bv = BitVector( bitstring = '110001' )
print("\nPrints out bits individually from bitstring 110001:")
print(bv[0], bv[1], bv[2], bv[3], bv[4], bv[5])       # 1 1 0 0 0 1
print("\nSame as above but using negative array indexing:")
print(bv[-1], bv[-2], bv[-3], bv[-4], bv[-5], bv[-6]) # 1 0 0 0 1 1

# Test setting bit values with positive and negative accessors:
bv = BitVector( bitstring = '1111' )
print("\nBitstring for 1111:")
print(bv)                                    # 1111

print("\nReset individual bits of above vector:")
bv[0]=0;bv[1]=0;bv[2]=0;bv[3]=0        
print(bv)                                    # 0000
print("\nDo the same as above with negative indices:")
bv[-1]=1;bv[-2]=1;bv[-4]=1
print(bv)                                    # 1011

print("\nCheck equality and inequality ops:")
bv1 = BitVector( bitstring = '00110011' )
bv2 = BitVector( bitlist = [0,0,1,1,0,0,1,1] )
print(bv1 == bv2)                           # True
print(bv1 != bv2)                           # False
print(bv1 < bv2)                            # False
print(bv1 <= bv2)                           # True
bv3 = BitVector( intVal = 5678 )
print(bv3.intValue())                       # 5678
print(bv3)                                  # 1011000101110
print(bv1 == bv3)                           # False
print(bv3 > bv1)                            # True
print(bv3 >= bv1)                           # True

# Write a bit vector to a file like object
fp_write = io.StringIO()
bv.write_bits_to_fileobject( fp_write )
print("\nGet bit vector written out to a file-like object:")
print(fp_write.getvalue())                  # 1011 

print("\nExperiments with bitwise logical operations:")
bv3 = bv1 | bv2                              
print(bv3)                                  # 00110011
bv3 = bv1 & bv2
print(bv3)                                  # 00110011
bv3 = bv1 + bv2
print(bv3)                                  # 0011001100110011
bv4 = BitVector( size = 3 )
print(bv4)                                  # 000
bv5 = bv3 + bv4
print(bv5)                                  # 0011001100110011000
bv6 = ~bv5
print(bv6)                                  # 1100110011001100111
bv7 = bv5 & bv6
print(bv7)                                  # 0000000000000000000
bv7 = bv5 | bv6
print(bv7)                                  # 1111111111111111111

print("\nTry logical operations on bit vectors of different sizes:")
print(BitVector( intVal = 6 ) ^ BitVector( intVal = 13 ))   # 1011
print(BitVector( intVal = 6 ) & BitVector( intVal = 13 ))   # 0100
print(BitVector( intVal = 6 ) | BitVector( intVal = 13 ))   # 1111

print(BitVector( intVal = 1 ) ^ BitVector( intVal = 13 ))   # 1100
print(BitVector( intVal = 1 ) & BitVector( intVal = 13 ))   # 0001
print(BitVector( intVal = 1 ) | BitVector( intVal = 13 ))   # 1101

print("\nExperiments with setbit() and len():")
bv7[7] = 0
print(bv7)                                   # 1111111011111111111
print(len( bv7 ))                            # 19
bv8 = (bv5 & bv6) ^ bv7
print(bv8)                                   # 1111111011111111111

print("\nConstruct a bit vector from what is in the file testinput1.txt:")
bv = BitVector( filename = 'testinput1.txt' )
#print bv                                    # nothing to show
bv1 = bv.read_bits_from_file(64)    
print("\nPrint out the first 64 bits read from the file:")
print(bv1)
     # 0100000100100000011010000111010101101110011001110111001001111001
print("\nRead the next 64 bits from the same file:")
bv2 = bv.read_bits_from_file(64)    
print(bv2)
     # 0010000001100010011100100110111101110111011011100010000001100110
print("\nTake xor of the previous two bit vectors:")
bv3 = bv1 ^ bv2
print(bv3)
     # 0110000101000010000110100001101000011001000010010101001000011111

print("\nExperiment with dividing an even-sized vector into two:")
[bv4, bv5] = bv3.divide_into_two()
print(bv4)                            # 01100001010000100001101000011010
print(bv5)                            # 00011001000010010101001000011111

# Permute a bit vector:
print("\nWe will use this bit vector for experiments with permute()")
bv1 = BitVector( bitlist = [1, 0, 0, 1, 1, 0, 1] )
print(bv1)                                    # 1001101

bv2 = bv1.permute( [6, 2, 0, 1] )
print("\nPermuted and contracted form of the previous bit vector:")
print(bv2)                                    # 1010

print("\nExperiment with writing an internally generated bit vector out to a disk file:")
bv1 = BitVector( bitstring = '00001010' ) 
FILEOUT = open( 'test.txt', 'wb' )
bv1.write_to_file( FILEOUT )
FILEOUT.close()
bv2 = BitVector( filename = 'test.txt' )
bv3 = bv2.read_bits_from_file( 32 )
print("\nDisplay bit vectors written out to file and read back from the file and their respective lengths:")
print( str(bv1) + " " + str(bv3))
print(str(len(bv1)) + " " + str(len(bv3)))

print("\nExperiments with reading a file from the beginning to end:")
bv = BitVector( filename = 'testinput4.txt' )
print("\nHere are all the bits read from the file:")
while (bv.more_to_read):
    bv_read = bv.read_bits_from_file( 64 )
    print(bv_read)
print("\n")

print("\nExperiment with closing a file object and start extracting bit vectors from the file from the beginning again:")
bv.close_file_object()
bv = BitVector( filename = 'testinput4.txt' )
bv1 = bv.read_bits_from_file(64)        
print("\nHere are all the first 64 bits read from the file again after the file object was closed and opened again:")
print(bv1)
FILEOUT = open( 'testinput5.txt', 'wb' )
bv1.write_to_file( FILEOUT )
FILEOUT.close()

print("\nExperiment in 64-bit permutation and unpermutation of the previous 64-bit bitvector:")
print("The permutation array was generated separately by the Fisher-Yates shuffle algorithm:")
bv2 = bv1.permute( [22, 47, 33, 36, 18, 6, 32, 29, 54, 62, 4,
                    9, 42, 39, 45, 59, 8, 50, 35, 20, 25, 49,
                    15, 61, 55, 60, 0, 14, 38, 40, 23, 17, 41,
                    10, 57, 12, 30, 3, 52, 11, 26, 43, 21, 13,
                    58, 37, 48, 28, 1, 63, 2, 31, 53, 56, 44, 24,
                    51, 19, 7, 5, 34, 27, 16, 46] )
print("Permuted bit vector:")
print(bv2)

bv3 = bv2.unpermute( [22, 47, 33, 36, 18, 6, 32, 29, 54, 62, 4,
                      9, 42, 39, 45, 59, 8, 50, 35, 20, 25, 49,
                      15, 61, 55, 60, 0, 14, 38, 40, 23, 17, 41,
                      10, 57, 12, 30, 3, 52, 11, 26, 43, 21, 13,
                      58, 37, 48, 28, 1, 63, 2, 31, 53, 56, 44, 24,
                      51, 19, 7, 5, 34, 27, 16, 46] )    
print("Unpurmute the bit vector:")
print(bv3)

print("\nTry circular shifts to the left and to the right for the following bit vector:")
print(bv3)   # 0100000100100000011010000111010101101110011001110111001001111001
print("\nCircular shift to the left by 7 positions:")
bv3 << 7
print(bv3)   # 1001000000110100001110101011011100110011101110010011110010100000

print("\nCircular shift to the right by 7 positions:")
bv3 >> 7
print(bv3)   # 0100000100100000011010000111010101101110011001110111001001111001

print("Test len() on the above bit vector:")
print(len( bv3 ))                      # 64

print("\nTest forming a [5:22] slice of the above bit vector:")
bv4 = bv3[5:22]
print(bv4)                             # 00100100000011010

print("\nTest the iterator:")
for bit in bv4:
    print(bit)                         # 0 0 1 0 0 1 0 0 0 0 0 0 1 1 0 1 0

print("\nDemonstrate padding a bit vector from left:")
bv = BitVector( bitstring = '101010' )
bv.pad_from_left( 4 )
print(bv)                              # 0000101010

print("\nDemonstrate padding a bit vector from right:")
bv.pad_from_right( 4 )
print(bv)                              # 00001010100000

print("\nTest the syntax 'if bit_vector_1 in bit_vector_2' syntax:")
try:
    bv1 = BitVector( bitstring = '0011001100' )
    bv2 = BitVector( bitstring = '110011' )
    if bv2 in bv1:
        print("%s is in %s" % (bv2, bv1))
    else:
        print("%s is not in %s" % (bv2, bv1))
except ValueError as arg:
    print("Error Message: " + str(arg))

print("\nTest the size modifier when a bit vector is initialized with the intVal method:")
bv = BitVector( intVal = 45, size = 16 )
print(bv)                             # 0000000000101101
bv = BitVector( intVal = 0, size = 8 )    
print(bv)                             # 00000000
bv = BitVector( intVal = 1, size = 8 )    
print(bv)                             # 00000001
print("\nTesting slice assignment:")
bv1 = BitVector( size = 25 )
print("bv1= " + str(bv1))             # 0000000000000000000000000
bv2 = BitVector( bitstring = '1010001' )
print("bv2= " + str(bv2))             # 1010001
bv1[6:9]  = bv2[0:3]
print("bv1= " + str(bv1))             # 0000001010000000000000000
bv1[:5] = bv1[5:10]
print("bv1= " + str(bv1))             # 0101001010000000000000000
bv1[20:] = bv1[5:10]
print("bv1= " + str(bv1))             # 0101001010000000000001010
bv1[:] = bv1[:]
print("bv1= " + str(bv1))             # 0101001010000000000001010
bv3 = bv1[:]
print("bv3= " + str(bv3))             # 0101001010000000000001010

print("\nTesting reset function:")
bv1.reset( 1 )             
print("bv1= " + str(bv1))             # 1111111111111111111111111
print(bv1[3:9].reset(0))              # 000000
print(bv1[:].reset(0))                # 0000000000000000000000000

print("\nTesting count_bit():")
bv = BitVector( intVal = 45, size = 16 )
y = bv.count_bits()
print(y)                              # 4
bv = BitVector( bitstring = '100111' )
print(bv.count_bits())                # 4
bv = BitVector( bitstring = '00111000' )
print(bv.count_bits())                # 3
bv = BitVector( bitstring = '001' )
print(bv.count_bits())                # 1
bv = BitVector( bitstring = '00000000000000' )
print(bv.count_bits())                # 0

print("\nTest setValue idea:")
bv = BitVector( intVal = 7, size =16 )
print(bv)                             # 0000000000000111
bv.setValue( intVal = 45 )
print(bv)                             # 101101

print("\nTesting count_bits_sparse():")
bv = BitVector( size = 2000000 )
bv[345234] = 1
bv[233]=1
bv[243]=1
bv[18]=1
bv[785] =1
print("The number of bits set: " + str(bv.count_bits_sparse()))    # 5

print("\nTesting Jaccard similarity and distance and Hamming distance:")
bv1 = BitVector( bitstring = '11111111' )
bv2 = BitVector( bitstring = '00101011' )
print("Jaccard similarity: " + str(bv1.jaccard_similarity( bv2 ))) # 0.5
print("Jaccard distance: " + str(bv1.jaccard_distance( bv2 )))     # 0.5
print("Hamming distance: " + str(bv1.hamming_distance( bv2 )))     # 4

print("\nTesting next_set_bit():")
bv = BitVector( bitstring = '00000000000001' )
print(bv.next_set_bit(5))                                    # 13
bv = BitVector( bitstring = '000000000000001' )
print(bv.next_set_bit(5))                                    # 14
bv = BitVector( bitstring = '0000000000000001' )
print(bv.next_set_bit(5))                                    # 15
bv = BitVector( bitstring = '00000000000000001' )
print(bv.next_set_bit(5))                                    # 16
bv = BitVector( bitstring = '00000000000000000' )
print(bv.next_set_bit(5))                                    # -1

print("\nTesting rank_of_bit_set_at_index():")
bv = BitVector( bitstring = '01010101011100' )
print(bv.rank_of_bit_set_at_index( 10 ))                     # 6

print("\nTesting isPowerOf2():")
bv = BitVector( bitstring = '10000000001110' )
print("int value: " + str(int(bv)))                          # 826
print(bv.isPowerOf2())                                       # False
print("\nTesting isPowerOf2_sparse():")              
print(bv.isPowerOf2_sparse())                                # False

print("\nTesting reverse():")
bv = BitVector( bitstring = '0001100000000000001' )
print("original bv: " + str(bv))             # 0001100000000000001
print("reversed bv: " + str(bv.reverse()))   # 1000000000000011000

print("\nTesting Greatest Common Divisor (gcd):")
bv1 = BitVector( bitstring = '01100110' )
print("first arg bv: " + str(bv1) + " of int value: " + str(int(bv1))) #102
bv2 = BitVector( bitstring = '011010' ) 
print("second arg bv: " + str(bv2) + " of int value: " + str(int(bv2)))# 26
bv = bv1.gcd( bv2 )
print("gcd bitvec is: " + str(bv) + " of int value: " + str(int(bv)))  # 2

print("\nTesting multiplicative_inverse:")
bv_modulus = BitVector( intVal = 32 )
print("modulus is bitvec: " + str(bv_modulus) + " of int value: " + str(int(bv_modulus)))
bv = BitVector( intVal = 17 ) 
print("bv: " + str(bv) + " of int value: " + str(int(bv)))
result = bv.multiplicative_inverse( bv_modulus )
if result is not None:
    print("MI bitvec is: " + str(result) + " of int value: " + str(int(result)))
else: print("No multiplicative inverse in this case")
                                                  # 17

print("\nTest multiplication in GF(2):")
#a = BitVector( bitstring='0110001' )
a = BitVector( bitstring='00000010' )

#b = BitVector( bitstring='0110' )
b = BitVector( bitstring='000001111' )

c = a.gf_multiply(b)
print("Product of a=" + str(a) + " b=" + str(b) + " is " + str(c))
                                                  # 10100110

#sys.exit(0)

print("\nTest division in GF(2^n):")
mod = BitVector( bitstring='100011011' )          # AES modulus
n = 8
a = BitVector( bitstring='11100010110001' )
quotient, remainder = a.gf_divide(mod, n)
print("Dividing a=" + str(a) + " by mod=" + str(mod) + " in GF(2^8) returns the quotient " + str(quotient) + " and the remainder " + str(remainder))

print("\nTest modular multiplication in GF(2^n):")
modulus = BitVector( bitstring='100011011' )     # AES modulus
n = 8
a = BitVector( bitstring='0110001' )
b = BitVector( bitstring='0110' )
c = a.gf_multiply_modular(b, modulus, n)
print("Modular product of a=" + str(a) + " b=" + str(b) + " in GF(2^8) is " + str(c))

print("\nTest multiplicative inverses in GF(2^3) with " + \
                               "modulus polynomial = x^3 + x + 1:")
print("Find multiplicative inverse of a single bit array")
modulus = BitVector( bitstring='100011011' )     # AES modulus
n = 8
a = BitVector( bitstring='00110011' )
mi = a.gf_MI(modulus,n)
print("Multiplicative inverse of " + str(a) + " in GF(2^8) is " + str(mi))

print("\nIn the following three rows shown, the first row shows the " +\
      "\nbinary code words, the second the multiplicative inverses," +\
      "\nand the third the product of a binary word with its" +\
      "\nmultiplicative inverse:\n")
mod = BitVector( bitstring = '1011' )
n = 3
bitarrays = [BitVector(intVal=x, size=n) for x in range(1,2**3)]
mi_list = [x.gf_MI(mod,n) for x in bitarrays]
mi_str_list = [str(x.gf_MI(mod,n)) for x in bitarrays]
print("bit arrays in GF(2^3): " + str([str(x) for x in bitarrays]))
print("multiplicati_inverses: " +  str(mi_str_list))

products = [ str(bitarrays[i].gf_multiply_modular(mi_list[i], mod, n)) \
                    for i in range(len(bitarrays)) ]
print("bit_array * multi_inv: " + str(products))

# UNCOMMENT THE FOLLOWING LINES FOR
# DISPLAYING ALL OF THE MULTIPLICATIVE 
# INVERSES IN GF(2^8) WITH THE AES MODULUS:

#    print("\nMultiplicative inverses in GF(2^8) with "  + \
#                      "modulus polynomial x^8 + x^4 + x^3 + x + 1:")
#    print("\n(This may take a few seconds)\n")
#    mod = BitVector( bitstring = '100011011' )
#    n = 8
#    bitarrays = [BitVector(intVal=x, size=n) for x in range(1,2**8)]
#    mi_list = [x.gf_MI(mod,n) for x in bitarrays]
#    mi_str_list = [str(x.gf_MI(mod,n)) for x in bitarrays]
#    print("\nMultiplicative Inverses:\n\n" + str(mi_str_list))
#    products = [ str(bitarrays[i].gf_multiply_modular(mi_list[i], mod, n)) \
#                        for i in range(len(bitarrays)) ]
#    print("\nShown below is the product of each binary code word " +\
#                     "in GF(2^3) and its multiplicative inverse:\n\n")
#    print(products)

print("\nExperimenting with runs():")
bv = BitVector( bitlist = (1, 0, 0, 1) )
print("For bit vector: " + str(bv))
print("       the runs are: " + str(bv.runs()))
bv = BitVector( bitlist = (1, 0) )
print("For bit vector: " + str(bv))
print("       the runs are: " + str(bv.runs()))
bv = BitVector( bitlist = (0, 1) )
print("For bit vector: " + str(bv))
print("       the runs are: " + str(bv.runs()))
bv = BitVector( bitlist = (0, 0, 0, 1) )
print("For bit vector: " + str(bv))
print("       the runs are: " + str(bv.runs()))
bv = BitVector( bitlist = (0, 1, 1, 0) )
print("For bit vector: " + str(bv))
print("       the runs are: " + str(bv.runs()))

print("\nExperiments with chained invocations of circular shifts:")
bv = BitVector( bitlist = (1,1, 1, 0, 0, 1) )
print(bv)
bv >> 1
print(bv)
bv >> 1 >> 1
print(bv)
bv = BitVector( bitlist = (1,1, 1, 0, 0, 1) )
print(bv)
bv << 1
print(bv)
bv << 1 << 1
print(bv)

print("\nExperiments with chained invocations of NON-circular shifts:")
bv = BitVector( bitlist = (1,1, 1, 0, 0, 1) )
print(bv)
bv.shift_right(1)
print(bv)
bv.shift_right(1).shift_right(1)
print(bv)
bv = BitVector( bitlist = (1,1, 1, 0, 0, 1) )
print(bv)
bv.shift_left(1)
print(bv)
bv.shift_left(1).shift_left(1)
print(bv)

# UNCOMMENT THE FOLLOWING LINES TO TEST THE
# PRIMALITY TESTING METHOD. IT SHOULD SHOW
# THAT ALL OF THE FOLLOWING NUMBERS ARE PRIME:
primes = [179, 233, 283, 353, 419, 467, 547, 607, 661, 739, 811, 877, \
          947, 1019, 1087, 1153, 1229, 1297, 1381, 1453, 1523, 1597, \
          1663, 1741, 1823, 1901, 7001, 7109, 7211, 7307, 7417, 7507, \
          7573, 7649, 7727, 7841]
for p in primes:
    bv = BitVector( intVal = p )
    check = bv.test_for_primality()
    print("The primality test for " + str(p) + ": " + str(check))

print("\nGenerate 32-bit wide candidate for primality testing:")
bv = BitVector( intVal = 0 )
bv = bv.gen_random_bits(32)
print(bv)
check = bv.test_for_primality()
print("The primality test for " + str(int(bv)) + ": " + str(check))    


import BitVector
import unittest
import io
import sys

constructorTests = [
    (('size','0'), ''),
    (('size','1'), '0'), 
    (('bitlist','(1,1,0,1)'), '1101'),
    (('bitlist', '[1,0,0,1]'), '1001'),    
    (('intVal', '5678'), '1011000101110'),    
    (('bitstring', '00110011'), '00110011'),
    (('streamobject', '111100001111'), '111100001111'),
    (('filename', 'testinput1.txt'), '0100000100100000011010000111010101101110011001110111001001111001'),
    ]

class ConstructorTestCases(unittest.TestCase):
    def checkConstructors(self):
        print("\nTesting constructors")
        for args, expected in constructorTests:
            try:
                mode = args[0]
                if (mode == 'size'):
                    bitvec = BitVector.BitVector( size = eval(args[1]) )
                elif (mode == 'bitlist'):
                    bitvec = BitVector.BitVector( bitlist = eval(args[1]) )
                elif (mode == 'intVal'):
                    bitvec = BitVector.BitVector( intVal = int(args[1]) )
                elif (mode == 'bitstring'):
                    bitvec = BitVector.BitVector( bitstring = args[1] )
                elif (mode == 'streamobject'):
                    fp_read = None 
                    if sys.version_info[0] == 3:
                        fp_read = io.StringIO(args[1])
                    else:
                        fp_read = io.StringIO( unicode(args[1]) )
                    bitvec = BitVector.BitVector( fp = fp_read )
                elif (mode == 'filename'):
                    bvec   = BitVector.BitVector( filename = args[1] )
                    bitvec = bvec.read_bits_from_file(64)    
                actual = str(bitvec)
                assert expected == actual
            except Exception as e:
                print(e)
                print("        CONSTRUCTOR TEST FAILED")

def getTestSuites(type):
    return unittest.TestSuite([
            unittest.makeSuite(ConstructorTestCases, type)
                ])                    

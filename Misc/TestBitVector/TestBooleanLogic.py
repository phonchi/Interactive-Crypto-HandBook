import BitVector
import unittest

bv1 = BitVector.BitVector( bitstring = '00110011' )
bv2 = BitVector.BitVector( bitlist = [1,1,1,1,0,0,1,1] )
bv3 = BitVector.BitVector( bitstring = '00000000111111110000000' )
bv4 = BitVector.BitVector( bitstring = '' )
bv5 = BitVector.BitVector( size = 0 )



logicTests = [
    ((bv1,bv2, '&'), '00110011'),
    ((bv1,bv3, '&'), ''),
    ((bv1,bv4, '&'), ''),
    ((bv1,bv5, '&'), ''),
    ((bv1,bv2, '|'), '11110011'),
    ((bv1,bv3, '|'), ''),
    ((bv1,bv4, '|'), ''),
    ((bv1,bv5, '|'), ''),
    ((bv1,'', '~'), '11001100'),
    ]

class BooleanLogicTestCase(unittest.TestCase):
    def checkLogicOp(self):
        print("\nTesting Boolean operators") 
        for args, expected in logicTests:
            try:
                op = args[2]
                if (op == '&'):
                    actual = args[0] & args[1]
                elif (op == '|'):
                    actual = args[0] | args[1]
                elif (op == '~'):
                    actual =  ~args[0]
                assert actual == BitVector.BitVector( bitstring = expected )
            except Exception as e:
                if ( args[0].size == args[1].size ):
                    print(e)
                    print("        BOOLEAN LOGIC TEST FAILED")

def getTestSuites(type):
    return unittest.TestSuite([
            unittest.makeSuite(BooleanLogicTestCase, type)
                ])                    

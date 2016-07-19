import BitVector
import unittest

bv = BitVector.BitVector( bitstring = '00110011' )

circularShiftTests = [
    ((3, '>>'), '01100110'),
    ((3, '<<'), '10011001'),
    ]

class CircularShiftTestCase(unittest.TestCase):
    def checkCircularShifts(self):
        print("\nTesting CircularShifts")
        for args, expected in circularShiftTests:
            try:
                op = args[1]
                if (op == '>>'):
                    actual = BitVector.BitVector( bitstring = str(bv) )
                    actual >> args[0]
                elif (op == '<<'):
                    actual = BitVector.BitVector( bitstring = str(bv) )
                    actual << args[0]
                assert actual == BitVector.BitVector( bitstring = expected )
            except Exception as e:
                print(e)
                print("        CIRCULAR SHIFT TEST FAILED")

def getTestSuites(type):
    return unittest.TestSuite([
            unittest.makeSuite(CircularShiftTestCase, type)
                ])                    

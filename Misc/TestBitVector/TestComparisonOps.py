import BitVector
import unittest

bv1 = BitVector.BitVector( bitstring = '00110011' )
bv2 = BitVector.BitVector( bitlist = [0,0,1,1,0,0,1,1] )
bv3 = BitVector.BitVector( intVal = 5678 )

comparisonTests = [
    ((bv1,bv2, '=='), True),
    ((bv1,bv2, '!='), False),
    ((bv1,bv2, '<'), False),
    ((bv1,bv2, '<='), True),
    ((bv1,bv3, '=='), False),
    ((bv3,bv1, '>'), True),
    ((bv3,bv1, '>='), True),
    ]

class ComparisonTestCases(unittest.TestCase):
    def checkComparisons(self):
        print("\nTesting comparison operators")
        for args, expected in comparisonTests:
            try:
                op = args[2]
                if (op == '=='):
                    actual = args[0] == args[1]
                elif (op == '!='):
                    actual = args[0] != args[1]
                elif (op == '<'):
                    actual = args[0] < args[1]
                elif (op == '<='):
                    actual = args[0] <= args[1]
                elif (op == '=='):
                    actual = args[0] == args[1]
                elif (op == '>'):
                    actual = args[0] > args[1]
                elif (op == '>='):
                    actual = args[0] >= args[1]
                assert expected == actual
            except Exception as e:
                print(e)
                print("        COMPARISON TEST FAILED")

def getTestSuites(type):
    return unittest.TestSuite([
            unittest.makeSuite(ComparisonTestCases, type)
                             ])                    

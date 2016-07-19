import BitVector
import unittest

bv1 = BitVector.BitVector( bitlist = [1,0,0,1,1,0,1] )
bv2 = BitVector.BitVector( bitlist = [1,0,1,0,0,1,1] )

permutationTests = [
    ((bv1, 'permute', '6201543'), '1010011'),
    ((bv2, 'unpermute', '6201543'), '1001101'),
    ]

class PermutationTestCase(unittest.TestCase):
    def checkPermutations(self):
        print("\nTesting permutations")
        for args, expected in permutationTests:
            try:
                if (args[1] == 'permute'):
                    actual = args[0].permute( list(map( lambda x: int(x),
                                                   list( args[2] ) ) ) ) 
                elif (args[1] == 'unpermute'):
                    actual = args[0].unpermute( list(map( lambda x: int(x),
                                                     list( args[2] ) ) ) )
                assert actual == BitVector.BitVector( bitstring = expected )
            except Exception as e:
                print(e)
                print("Permutation test failed")

def getTestSuites(type):
    return unittest.TestSuite([
            unittest.makeSuite(PermutationTestCase, type)
                ])                    

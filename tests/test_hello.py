import unittest
import sys 
from io import StringIO


from snot.hello import HELLO

class TestHello(unittest.TestCase):


    def testworks(self):
        out = StringIO()
        sys.stdout = out

        HELLO.run()

        sys.stdout = sys.__stdout__

        output = out.getvalue()

        self.assert_(output == 'me\n')



if __name__ == '__main__':
    unittest.main()

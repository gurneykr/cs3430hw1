#!/usr/bin/python

#######################################
# module: unit_tests.py
# description: examples of unit tests
# bugs to vladimir kulyukin via canvas
#######################################

import unittest
from prod import prod
from maker import make_const, make_pwr
from tof import tof
from deriv import deriv

class DerivUnitTests(unittest.TestCase):

    def test_01(self):
        print ('\n***** Unit Test 01 ************')
        fex = prod(mult1=make_const(6.0),
                   mult2=make_pwr('x', 3.0))
        drv = deriv(fex)
        print(drv)

        assert not drv is None
        drvf = tof(drv)
        print("deriv(1):", drvf(1))
        print("deriv(2):", drvf(2))
        print("deriv(3):", drvf(3))
        print("deriv(4):", drvf(4))
        assert not drvf is None
        gt = lambda x: 18*(x**2)
        err = 0.00001
        for i in range(1, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print ('Unit Test 02: pass')

    def test_02(self):
        print ('\n***** Unit Test 02 ************')
        fex = prod(mult1=make_const(3.0),
                   mult2=make_pwr('x', 1.0/3.0))
        drv = deriv(fex)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: (x**(-2.0/3.0))
        err = 0.00001
        for i in range(1, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print ('Unit Test 02: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()

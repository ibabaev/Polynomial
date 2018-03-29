import unittest
from Polynomial import Polynomial

class MyTestCase(unittest.TestCase):

    def test_TypeError(self):
        self.assertRaises(TypeError, Polynomial, [])
        self.assertRaises(TypeError, Polynomial, ['x', 'y'])
        self.assertRaises(TypeError, Polynomial, ['x', 42])
        self.assertRaises(TypeError, Polynomial.__add__, Polynomial([4, 2]), "x")
        self.assertRaises(TypeError, Polynomial.__mul__, Polynomial([4, 2]), "x")
        self.assertRaises(TypeError, Polynomial.__eq__, Polynomial([4, 2]), "x")

    def test_add_int(self):
        p1 = Polynomial([4, 3, 2, 1])
        p2 = Polynomial([3, 2, 1])
        self.assertEqual((p1 + p2).coeffs, [4, 6, 4, 2])
        self.assertEqual((p2 + p1).coeffs, [4, 6, 4, 2])

    def test_add_negative_int(self):
        p1 = Polynomial([4, 3, 2, 1])
        p2 = Polynomial([-3, -2, -1])
        self.assertEqual((p1 + p2).coeffs, [4, 0, 0, 0])
        self.assertEqual((p2 + p1).coeffs, [4, 0, 0, 0])

    def test_sub_int(self):
        p1 = Polynomial([4, 3, 2, 1])
        p2 = Polynomial([3, 2, 1])
        self.assertEqual((p1 - p2).coeffs, [4, 0, 0, 0])
        self.assertEqual((p2 - p1).coeffs, [-4, 0, 0, 0])

    def test_add_int_const(self):
        p1 = Polynomial([4, 3, 2, 1])
        c = 9
        self.assertEqual((p1 + c).coeffs, [4, 3, 2, 10])
        self.assertEqual((c + p1).coeffs, [4, 3, 2, 10])

    def test_add_int_negative_const(self):
        p1 = Polynomial([4, 3, 2, 1])
        c = -9
        self.assertEqual((p1 + c).coeffs, [4, 3, 2, -8])
        self.assertEqual((c + p1).coeffs, [4, 3, 2, -8])

    def test_sub_int_const(self):
        p1 = Polynomial([4, 3, 2, 1])
        c = 9
        self.assertEqual((p1 - c).coeffs, [4, 3, 2, -8])
        self.assertEqual((-c + p1).coeffs, [4, 3, 2, -8])

    def test_add_begining_null_polynom(self):
        p1 = Polynomial([0, 0, 0, 4, 3, 2, 1])
        p2 = Polynomial([0, 0, 0, 3, 2, 1])
        self.assertEqual((p1 + p2).coeffs, [4, 6, 4, 2])
        self.assertEqual((p2 + p1).coeffs, [4, 6, 4, 2])

    def test_sub_begining_null_polynom(self):
        p1 = Polynomial([0, 0, 0, 4, 3, 2, 1])
        p2 = Polynomial([0, 0, 0, 3, 2, 1])
        self.assertEqual((p1 - p2).coeffs, [4, 0, 0, 0])
        self.assertEqual((p2 - p1).coeffs, [-4, 0, 0, 0])

    def test_add_zero_polynom(self):
        p1 = Polynomial([4, 3, 2, 1])
        p2 = Polynomial([0, 0, 0])
        self.assertEqual((p1 + p2).coeffs, [4, 3, 2, 1])
        self.assertEqual((p2 + p1).coeffs, [4, 3, 2, 1])

    def test_sub_zero_polynom(self):
        p1 = Polynomial([4, 3, 2, 1])
        p2 = Polynomial([0, 0, 0])
        self.assertEqual((p1 - p2).coeffs, [4, 3, 2, 1])
        self.assertEqual((p2 - p1).coeffs, [-4, -3, -2, -1])

    def test_mult_zero_polynom(self):
        p1 = Polynomial([4, 3, 2, 1])
        p2 = Polynomial([0, 0, 0])
        self.assertEqual((p1 * p2).coeffs, [0])
        self.assertEqual((p2 * p1).coeffs, [0])

    def test_mult_zero_const(self):
        p1 = Polynomial([4, 3, 2, 1])
        p2 = 0
        self.assertEqual((p1 * p2).coeffs, [0])
        self.assertEqual((p2 * p1).coeffs, [0])

    def test_multiplay_int(self):
        p1 = Polynomial([1, -1])
        p2 = Polynomial([1, 1])
        self.assertEqual((p1 * p2).coeffs, [1, 0, -1])
        self.assertEqual((p2 * p1).coeffs, [1, 0, -1])

    def test_multiplay_int_const(self):
        p1 = Polynomial([3, 2, 1])
        p2 = 2
        self.assertEqual((p1 * p2).coeffs, [6, 4, 2])
        self.assertEqual((p2 * p1).coeffs, [6, 4, 2])

    def test_add_float(self):
        p1 = Polynomial([4.1, 3.5, 2.1, 1])
        p2 = Polynomial([3.5, 2, 1])
        self.assertEqual((p1 + p2).coeffs, [4.1, 7, 4.1, 2])
        self.assertEqual((p2 + p1).coeffs, [4.1, 7, 4.1, 2])

    def test_add_negative_float(self):
        p1 = Polynomial([4.1, 3.3, 2.2, 1.5])
        p2 = Polynomial([-3.3, -2.2, -1])
        self.assertEqual((p1 + p2).coeffs, [4.1, 0, 0, 0.5])
        self.assertEqual((p2 + p1).coeffs, [4.1, 0, 0, 0.5])

    def test_sub_float(self):
        p1 = Polynomial([4.1, 3.4, 2.3, 2.11])
        p2 = Polynomial([3.4, 2.3, 2.11])
        self.assertEqual((p1 - p2).coeffs, [4.1, 0, 0, 0])
        self.assertEqual((p2 - p1).coeffs, [-4.1, 0, 0, 0])

    def test_add_float_const(self):
        p1 = Polynomial([4.1, 3, 2, 1])
        c = 9.6
        self.assertEqual((p1 + c).coeffs, [4.1, 3, 2, 10.6])
        self.assertEqual((c + p1).coeffs, [4.1, 3, 2, 10.6])

    def test_add_float_negative_const(self):
        p1 = Polynomial([4, 3, 2, 1])
        c = -9.6
        self.assertEqual((p1 + c).coeffs, [4, 3, 2, -8.6])
        self.assertEqual((c + p1).coeffs, [4, 3, 2, -8.6])

    def test_sub_float_const(self):
        p1 = Polynomial([4, 3, 2, 1])
        c = 9.6
        self.assertEqual((p1 - c).coeffs, [4, 3, 2, -8.6])
        self.assertEqual((-c + p1).coeffs, [4, 3, 2, -8.6])

    def test_multiplay_float_const(self):
        p1 = Polynomial([3.2, 2.1, 1.4])
        p2 = 2
        self.assertEqual((p1 * p2).coeffs, [6.4, 4.2, 2.8])
        self.assertEqual((p2 * p1).coeffs, [6.4, 4.2, 2.8])

    def test_string(self):
        p1 = Polynomial([0])
        self.assertEqual(str(p1), "0")
        p1 = Polynomial([0, 0, 0])
        self.assertEqual(str(p1), "0")
        p1 = Polynomial([-3, 2, 0])
        self.assertEqual(str(p1), "-3x2+2x")
        p1 = Polynomial([0, -2, 1])
        self.assertEqual(str(p1), "-2x+1")
        p1 = Polynomial([-4, 3, 2, 1])
        self.assertEqual(str(p1), "-4x3+3x2+2x+1")

    def test_string_float(self):
        p1 = Polynomial([0.0])
        self.assertEqual(str(p1), "0")
        p1 = Polynomial([0.0, 0.0, 0.0])
        self.assertEqual(str(p1), "0")
        p1 = Polynomial([3.3, -2.2, 1.5])
        self.assertEqual(str(p1), "3.3x2-2.2x+1.5")
        p1 = Polynomial([-4.1, 3.3, -2.2, 1.5])
        self.assertEqual(str(p1), "-4.1x3+3.3x2-2.2x+1.5")

if __name__ == '__main__':
    unittest.main()
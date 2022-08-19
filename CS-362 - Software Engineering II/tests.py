import unittest
from task import conv_num, conv_endian, my_datetime


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertEqual(conv_num('12345'), 12345)

    def test2(self):
        self.assertEqual(conv_num('-123.45'), -123.45)

    def test3(self):
        self.assertEqual(conv_num('.45'), .45)

    def test4(self):
        self.assertEqual(conv_num('123.'), 123.0)

    def test5(self):
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test6(self):
        self.assertEqual(conv_num('0xAZ4'), None)

    def test7(self):
        self.assertEqual(conv_num('12345A'), None)

    def test8(self):
        self.assertEqual(conv_num('12.3.45'), None)

    def test9(self):
        self.assertEqual(conv_num(''), None)

    def test10(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test11(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test12(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test13(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test14(self):
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test15(self):
        self.assertEqual(conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    def test16(self):
        self.assertEqual(conv_endian(num=-954786, endian='small'), None)

    def test17(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test18(self):
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    def test19(self):
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

    def test20(self):
        self.assertEqual(my_datetime(201653971200), "02-29-8360")


if __name__ == '__main__':
    unittest.main()

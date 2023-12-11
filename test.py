import unittest
from main import аrchiver
from main import unpacker

class UnzipCorrectTestCase(unittest.TestCase):

    def test_аrchiver(self):
        test_str = "This 2023 string serves as 2023 example for LZW 2023 string compression method"
        unpacked_str = unpacker(аrchiver(test_str))
        self.assertEqual(unpacked_str, test_str)

    def test_аrchiver(self):
        test_str = "Swarm B vector (VFM) and scalar (ASM) magnetic field measurements interpolated at 1Hz rate"
        unpacked_str = unpacker(аrchiver(test_str))
        self.assertEqual(unpacked_str, test_str)


if __name__ == '__main__':
    unittest.main()

class CompressionTestCase(unittest.TestCase):

    def test_аrchiver(self):
        test_str = "This 2023 string serves as 2023 example for LZW 2023 string compression method"
        len_before = len(test_str)
        len_after = len(аrchiver(test_str))
        self.assertTrue(len_before > len_after)

    def test_аrchiver(self):
        test_str = "Swarm B vector (VFM) and scalar (ASM) magnetic field measurements interpolated at 1Hz rate"
        len_before = len(test_str)
        len_after = len(аrchiver(test_str))
        self.assertTrue(len_before > len_after)

if __name__ == '__main__':
    unittest.main()
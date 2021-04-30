import unittest
import HW4

class TestCase(unittest.TestCase):
    def test1(self):
        #with self.assertRaises(AssertionError):
        self.assertEqual(HW4.find_cube_volume(-2),8)

    def test2(self):
        #with self.assertRaises(AssertionError):
        self.assertEqual(HW4.find_cube_volume(complex(2,3)),8)

    def test3(self):
        #with self.assertRaises(TypeError):
        self.assertEqual(HW4.find_cube_volume("2"),8)

    def test4(self):
        self.assertEqual(HW4.find_cube_volume(2),8)

    def test5(self):
        #with self.assertRaises(ZeroDivisionError):
        self.assertEqual(HW4.list_average([]),2)

    def test6(self):
        #with self.assertRaises(TypeError):
        self.assertEqual(HW4.list_average(),0)

    def test7(self):
        #with self.assertRaises(TypeError):
        self.assertEqual(HW4.list_average(['4',4,4,4]),2)

    def test8(self):
        self.assertEqual(HW4.list_average([4,4,4,4]),4)

    def test9(self):
        #with self.assertRaises(AssertionError):
        self.assertEqual(HW4.full_name_generator(1,2),'12')

    def test10(self):
        #with self.assertRaises(TypeError):
        self.assertEqual(HW4.full_name_generator('2',3),'23')

    def test11(self):
        #with self.assertRaises(TypeError):
        self.assertEqual(HW4.full_name_generator(['h','i'],'burger'),'hiburger')

    def test12(self):
        self.assertEqual(HW4.full_name_generator('cheese','burger'),'cheeseburger')
if __name__ == '__main__':
    unittest.main(verbosity = 2)

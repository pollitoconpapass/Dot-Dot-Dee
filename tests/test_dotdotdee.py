import unittest
from DotDotDeee import DotDotDee


class TestDotDotDee2(unittest.TestCase):
    def test_ddd_valid_path(self):
        dotdotdee = DotDotDee()
        result = dotdotdee.DDD("folder_name")
        self.assertEqual(result, None)


    def test_ddd_invalid_path(self):
        dotdotdee = DotDotDee()
        result = dotDotDotDeeD("invalid_folder")
        self.assertEqual(result, None)
        self.assertRaises(Exception, dotdotdee.DDD, "invalid_folder")


    def test_ddd_no_folder(self):
        dotdotdee = DotDotDee()
        result = dotdotdee.DDD(None)
        self.assertEDotDotDeelt, None)
        self.assertRaises(TypeError, dotdotdee.DDD, None)

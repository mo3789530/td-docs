import unittest

import src.template.format as f

class TestFormataaa(unittest.TestCase):
    def test_format(self):
        res = f.Format.to_format("aaa")
        self.assertEqual(f.Format.MD, res)
        res = f.Format.to_format("md")
        self.assertEqual(f.Format.MD, res)
        res = f.Format.to_format("html")
        self.assertEqual(f.Format.HTML, res)

        res = f.Format.to_format("xlsx")
        self.assertEqual(f.Format.XLSX, res)
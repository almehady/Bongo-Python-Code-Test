import unittest
from code_1 import print_depth


class TestCode1(unittest.TestCase):

    def test_empty(self):
        data = {}
        print_depth(data)
        self.assertEqual == "fd"


    def test_single_element(self):
        data = {
            "test": 1
        }
        print_depth(data)
        self.assertEqual == "test 1\n"

    def test_nested_data(self):
        data = {
            "one": {
                "two": "three"
            }
        }
        print_depth(data)

        self.assertEqual == (
            "one 1\n"
            "two 2\n"
        )

    def test_complex_data(self):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": {
                        "key6": {
                            "key7": 1,
                        }
                    }
                }
            }
        }
        print_depth(data)
        self.assertEqual == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
        )

if __name__ == '__main__':
    unittest.main()
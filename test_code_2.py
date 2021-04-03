import unittest

from code_2 import print_depth, Person


class TestTask2(unittest.TestCase):

    def person_a(self):
        return Person("Paige", "Turner", None)

    def person_b(self, person_a):
        return Person("Walter", "Melon", person_a)

    def test_empty(self):
        data = {}
        print_depth(data)
        self.assertTrue == ""
        self.assertFalse == ""

    def test_single_dict(self):
        data = {
            "test": 1
        }
        print_depth(data)
        self.assertTrue == "test 1\n"
        self.assertFalse == ""

    def test_nested_dict(self):
        data = {
            "Turner": {
                "Melon": "three"
            }
        }
        print_depth(data)
        self.assertTrue == (
            "Turner 1\n"
            "Melon 2\n"
        )
        self.assertFalse == ""

    def test_multi_nested_dict(self):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        print_depth(data)
        self.assertTrue == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
        )
        self.assertFalse == ""


    def test_single_person(self, person_a):
        print_depth(person_a)
        self.assertTrue == (
            "Paige 1\n"
            "Turner 1\n"
            "None 1\n"
        )
        self.assertFalse == ""

    def test_nested_person(self, person_b):
        print_depth(person_b)
        self.assertTrue == (
            "Walter 1\n"
            "Melon 1\n"
            "Paige Turner 1\n"
            "Paige 2\n"
            "Turner 2\n"
            "None 2\n"
        )
        self.assertFalse == ""

    def test_mixed_data(self, person_b):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b,
                }
            },
        }
        print_depth(data)
        self.assertTrue == (
            "key1 1\n"
            "key2 1\n"
            "key3 2\n"
            "key4 2\n"
            "key5 3\n"
            "user 3\n"
            "Walter 4\n"
            "Melon 4\n"
            "Paige Turner 4\n"
            "Paige 5\n"
            "Turner 5\n"
            "None 5\n"
        )
        self.assertFalse == ""

if __name__ == '__main__':
    unittest.main()
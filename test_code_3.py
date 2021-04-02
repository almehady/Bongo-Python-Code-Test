import unittest
import code_3

class TestLca(unittest.TestCase):

    def test_node4_5(self):
        self.assertEqual(code_3.findLCA(code_3.root, 4, 5), 2)

    def test_node6_2(self):
        self.assertEqual(code_3.findLCA(code_3.root, 6, 2), 1)

    def test_node_none(self):
        self.assertEqual(code_3.findLCA(None, 4, 5), -1)

    def test_node1_5(self):
        self.assertEqual(code_3.findLCA(code_3.root, 1, 5), 1)

    def test_node_same(self):
        self.assertEqual(code_3.findLCA(code_3.root, 1, 1), 1)

    def test_node2_3(self):
        self.assertEqual(code_3.findLCA(code_3.root, 2, 3), 1)

    def test_node6_7(self):
        self.assertEqual(code_3.findLCA(code_3.root, 6, 7), 3)

    def test_node_fake(self):
        self.assertEqual(code_3.findLCA(code_3.root, 8, 8), -1)


if __name__ == '__main__':
    unittest.main()
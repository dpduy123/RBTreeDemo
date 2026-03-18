import unittest
from rbtree import RedBlackTree

class TestRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.tree = RedBlackTree()

    def test_root_is_black(self):
        self.tree.insert(10)
        self.assertEqual(self.tree.root.color, 0)

    def test_no_double_red(self):
        keys = [10, 20, 30, 15, 25]
        for k in keys:
            self.tree.insert(k)
        
        def check_no_double_red(node):
            if node == self.tree.T_NIL:
                return
            if node.color == 1:
                self.assertEqual(node.left.color, 0)
                self.assertEqual(node.right.color, 0)
            check_no_double_red(node.left)
            check_no_double_red(node.right)

        check_no_double_red(self.tree.root)

    def test_black_height(self):
        keys = [10, 20, 30, 40, 50, 60, 70, 80]
        for k in keys:
            self.tree.insert(k)

        def get_black_height(node):
            if node == self.tree.T_NIL:
                return 1
            left_height = get_black_height(node.left)
            right_height = get_black_height(node.right)
            self.assertEqual(left_height, right_height)
            return left_height + (1 if node.color == 0 else 0)

        get_black_height(self.tree.root)

    def test_search(self):
        self.tree.insert(10)
        self.tree.insert(20)
        self.assertNotEqual(self.tree.search(self.tree.root, 10), self.tree.T_NIL)
        self.assertNotEqual(self.tree.search(self.tree.root, 20), self.tree.T_NIL)
        self.assertEqual(self.tree.search(self.tree.root, 30), self.tree.T_NIL)

if __name__ == '__main__':
    unittest.main()

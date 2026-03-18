import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1  # 1 for Red, 0 for Black

class RedBlackTree:
    def __init__(self):
        self.T_NIL = Node(0)
        self.T_NIL.color = 0
        self.T_NIL.left = None
        self.T_NIL.right = None
        self.root = self.T_NIL

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.T_NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.T_NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.T_NIL
        node.right = self.T_NIL
        node.color = 1  # New node is always red

        y = None
        x = self.root

        while x != self.T_NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self._insert_fixup(node)

    def _insert_fixup(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def search(self, node, key):
        if node == self.T_NIL or key == node.data:
            return node

        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def print_tree(self, node, indent="", last=True):
        if node != self.T_NIL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("└─")
                indent += "  "
            else:
                sys.stdout.write("├─")
                indent += "│ "

            color = "RED" if node.color == 1 else "BLACK"
            print(f"{node.data}({color})")

            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

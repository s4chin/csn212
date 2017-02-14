RED = 1
BLACK = 0

class Node:
    def __init__(self, low, high, color = BLACK):
        self.lo = low
        self.hi = high
        self.color = color
        self.key = self.lo # Keyed on low
        self.max = self.hi
        self.p = None
        self.left = None
        self.right = None

    def __repr__(self):
        if self.lo is not None:
            return "[{0}, {1}], color: {2}, max: {3}".format(self.lo, self.hi, "BLACK" if self.color == 0 else "RED", self.max)
        return "Sentinel empty node"

class IntervalTree:
    def __init__(self, nodeList = []):
        self.nil = Node(None, None)
        self.root = self.nil
        for node in nodeList:
            self.insertNode(node)

    def insertNode(self, z):
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if z.max > x.max:  # Edit max of node
                x.max = z.max
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = RED
        self.insertFixup(z)

    def insertFixup(self, z):
        while z.p.color == RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.leftRotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.rightRotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.leftRotate(z.p.p)
        self.root.color = BLACK

    def transplant(self, u, v):
        if u.p is self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def deleteNode(self, z):
        y = z
        y_original_color = y.color
        if z.left is self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.treeMinimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == BLACK:
            self.deleteFixup(x)

    def deleteFixup(x):
        while x != self.root and x.color == BLACK:
            if x == x.p.left:
                w = x.p.right
                if w.color == RED:
                    w.color = BLACK
                    x.p.xolor = RED
                    self.leftRotate(x.p)
                    w = x.p.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.p
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.rightRotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.right.color = BLACK
                    self.leftRotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.rightRotate(x.p)
                    w = x.p.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.p
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.leftRotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.left.color = BLACK
                    self.rightRotate(x.p)
                    x = self.root
            x.color = BLACK

    def intervalSearch(self, i):
        """
        Search overlapping node
        """
        x = self.root
        while x is not self.nil and (i.hi < x.lo or i.lo > x.hi):
            if x.left is not self.nil and x.left.max >= i.lo:
                x = x.left
            else:
                x = x.right
        print x.lo, x.hi
        return x

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.p = x
            ans = x.hi
            if x.left is not self.nil:
                if x.left.max > ans:
                    ans = x.left.max
            if x.right.max > ans:
                ans = x.right.max
            x.max = ans
        y.p = x.p
        if x.p is self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        ans = y.hi
        if y.right is not self.nil:
            if y.right.max > ans:
                ans = y.right.max
        if y.left.max > ans:
            ans = y.left.max
        y.max = ans

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.nil:
            y.right.p = x
            ans = x.hi
            if x.right is not self.nil:
                if x.right.max > ans:
                    ans = x.right.max
            if x.left.max > ans:
                ans = x.left.max
            x.max = ans
        y.p = x.p
        if x.p is self.nil:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
        ans = y.hi
        if y.left is not self.nil:
            if y.left.max > ans:
                ans = y.left.max
        if y.right.max > ans:
            ans = y.right.max
        y.max = ans

def printTree(x):
    if x.left:
        printTree(x.left)
    print x
    if x.right:
        printTree(x.right)

# This function to write the tree to file has been taken from http://code.activestate.com/recipes/576817-red-black-tree/
def write_tree_as_dot(t, f, show_nil=False):
    "Write the tree in the dot language format to f."
    def node_id(node):
        return 'N%d' % id(node)

    def node_color(node):
        if node.color == RED:
            return "RED"
        else:
            return "BLACK"

    def visit_node(node):
        "Visit a node."
        print >> f, "  %s [label=\"%s\", color=\"%s\"];" % (node_id(node), node, node_color(node))
        if node.left:
            if node.left != t.nil or show_nil:
                visit_node(node.left)
                print >> f, "  %s -> %s ;" % (node_id(node), node_id(node.left))
        if node.right:
            if node.right != t.nil or show_nil:
                visit_node(node.right)
                print >> f, "  %s -> %s ;" % (node_id(node), node_id(node.right))

    print >> f, "// Created by rbtree.write_dot()"
    print >> f, "digraph red_black_tree {"
    visit_node(t.root)
    print >> f, "}"

if __name__ == "__main__":
    intervals = [Node(15, 20), Node(10, 30), Node(17, 19), Node(5, 20), Node(12, 15), Node(30, 40)]
    t = IntervalTree(intervals)
    printTree(t.root)
    t.intervalSearch(Node(10, 15))
    t.insertNode(Node(13, 15))
    t.insertNode(Node(7, 10))
    t.intervalSearch(Node(13, 14))
    import os, sys
    def write_tree(t, filename):
        "Write the tree as an SVG file."
        f = open('%s.dot' % filename, 'w')
        write_tree_as_dot(t, f, True)
        f.close()
        os.system('dot %s.dot -Tsvg -o %s.svg' % (filename, filename))
    write_tree(t, 'tree')

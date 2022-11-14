from InorderSuccessor import Node, find_successor

testTree = Node(4)
testTree.left = Node(2)
testTree.right = Node(8)
testTree.left.parent = testTree
testTree.right.parent = testTree
testTree.left.left = Node(1)
testTree.left.left.parent = testTree.left
testTree.right.right = Node(7)
testTree.right.right.parent = testTree.right
testTree.right.left = Node(5)
testTree.right.left.parent = testTree.right
testTree.right.left.right = Node(7)
testTree.right.left.right.parent = testTree.right.left
testTree.right.right = Node(9)
testTree.right.right.parent = testTree.right

class TestSuite:
    def test_1(self):
        tree = Node(1)
        tree.right = Node(2)
        tree.right.parent = tree
        return find_successor(tree) == tree.right

    def test_2(self):
        tree = Node(2)
        tree.left = Node(1)
        tree.left.parent = tree
        tree.right = Node(3)
        tree.right.parent = tree
        return find_successor(tree.left) == tree

    def test_3(self):
        return find_successor(testTree.right) == testTree.right.right

    def test_4(self):
        return find_successor(testTree.left) == testTree

    def test_5(self):
        return find_successor(testTree.right.left.right) == testTree.right

    def test_6(self):
        return find_successor(testTree.right.left) == testTree.right.left.right

    def return_test_result(self, test_func):
        return "Passed" if test_func() else "Failed"

    def run_test_suite(self):
        print("Test results:")
        print("Test_1 : " + self.return_test_result(self.test_1))
        print("Test_2 : " + self.return_test_result(self.test_2))
        print("Test_3 : " + self.return_test_result(self.test_3))
        print("Test_4 : " + self.return_test_result(self.test_4))
        print("Test_5 : " + self.return_test_result(self.test_5))
        print("Test_6 : " + self.return_test_result(self.test_6))
        print("Test suite finished running")

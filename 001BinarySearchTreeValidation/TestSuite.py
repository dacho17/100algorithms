from ValidBinarySearchTree import Node, is_valid

class ValidBinarySearchTreeSuite:
    # Test 1
    #   5
    #  / \
    # 3   7
    def test_1(self):
        root = Node(5)
        root.left_node = Node(3)
        root.right_node = Node(7)
        return is_valid(root) == True
    # Expected: isValid = True

    # Test 2
    #   5
    #  / \
    # 7   3
    def test_2(self):
        root = Node(5)
        root.left_node = Node(7)
        root.right_node = Node(3)
        return is_valid(root) == False
    # Expected: isValid = False

    # Test 3
    #   5
    #  / \
    # 3   7
    #  \ 
    #   6
    def test_3(self):
        root = Node(5)
        root.left_node = Node(3)
        root.right_node = Node(7)
        root.left_node.right_node = Node(6)
        return is_valid(root) == False
    # Expected: isValid = False

    # Test 4
    #   5
    #  / \
    # 3   7
    #  \
    #   4
    def test_4(self):
        root = Node(5)
        root.left_node = Node(3)
        root.right_node = Node(7)
        root.left_node.right_node = Node(4)
        return is_valid(root) == True
    # Expected: isValid = True

    # Test 5
    #   5
    #  / \
    # 3   7
    #    /
    #   4
    def test_5(self):
        root = Node(5)
        root.left_node = Node(3)
        root.right_node = Node(7)
        root.right_node.left_node = Node(4)
        return is_valid(root) == False
    # Expected: isValid = False

    # Test 6
    #   5
    #  / \
    # 3   7
    #    /
    #   6
    def test_6(self):
        root = Node(5)
        root.left_node = Node(3)
        root.right_node = Node(7)
        root.right_node.left_node = Node(6)
        return is_valid(root) == True
    # Expected: isValid = True

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

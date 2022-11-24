from BalancedBinaryTrees import Node, is_tree_height_balanced


class TestSuite:
    def test_1(self):
        return is_tree_height_balanced(Node())[0] == True

    def test_2(self):
        return is_tree_height_balanced(Node(None, Node()))[0] == True

    def test_3(self):
        return is_tree_height_balanced(Node(Node(), None))[0] == True

    def test_4(self):
        return is_tree_height_balanced(Node(Node(), Node()))[0] == True

    def test_5(self):
        return is_tree_height_balanced(Node(Node(Node(), Node()), None))[0] == False

    def test_6(self):
        return is_tree_height_balanced(Node(Node(Node()), Node()))[0] == True

    def test_7(self):
        return is_tree_height_balanced(Node(Node(Node(), Node(Node(None, Node()))), Node(None, Node())))[0] == False

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
        print("Test_7 : " + self.return_test_result(self.test_7))
        print("Test suite finished running")

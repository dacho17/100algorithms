from FilterLeavesOfaBinaryTree import Node, prune_lower_than, serialize_bin_tree

class TestSuite:
    def test_1(self):
        return serialize_bin_tree(prune_lower_than(Node(1), 1)) == "1##"

    def test_2(self):
        return serialize_bin_tree(prune_lower_than(Node(1, Node(2), Node(3)), 1)) == "1##"

    def test_3(self):
        return serialize_bin_tree(prune_lower_than(Node(1, Node(1), Node(1)), 1)) == "11##1##"

    def test_4(self):
        return serialize_bin_tree(prune_lower_than(Node(3, Node(2, Node(2)), Node(3, Node(1))), 3)) == "3#3##"

    def test_5(self):
        return serialize_bin_tree(prune_lower_than(Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6, Node(7), Node(8)))), 0)) == "#"

    def test_6(self):
        return serialize_bin_tree(prune_lower_than(Node(1, Node(2, None, Node(5, Node(7))), Node(5, Node(4), Node(3))), 5)) == "12#5##5##"

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

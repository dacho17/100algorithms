from FrequentSubtreeSum import Node, find_most_frequent_subtree_sum

class TestSuite:
    def test_1(self):
        return find_most_frequent_subtree_sum(Node(1)) == (1, 1)

    def test_2(self):
        return find_most_frequent_subtree_sum(Node(1, Node(1), Node(1))) == (1, 2)

    def test_3(self):
        return find_most_frequent_subtree_sum(Node(1, None, Node(0, Node(2, Node(0), Node(2))))) == (4, 2)

    def test_4(self):
        return find_most_frequent_subtree_sum(Node(0, Node(0, None, Node(5)), Node(0))) == (5, 3)

    def test_5(self):
        return find_most_frequent_subtree_sum(Node(1, Node(1, None, Node(7, None, Node(-9))), Node(-2, Node(2, Node(-2))))) == (-2, 4)

    def test_6(self):
        return find_most_frequent_subtree_sum(Node(4, Node(3, Node(-3, Node(12), Node(-7))), Node(0, Node(0), Node(-5, Node(5), Node(5))))) == (5, 5)

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

#       4
#      3 0      2
#    -3 0-5     1
#   12-7 5 5    2

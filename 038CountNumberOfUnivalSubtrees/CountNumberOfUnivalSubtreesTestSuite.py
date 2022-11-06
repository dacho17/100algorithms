from CountNumberOfUnivalSubtrees import Node, count_unival_subtrees

class TestSuite:
    def test_1(self):
        return count_unival_subtrees(Node(1))[2] == 1

    def test_2(self):
        return count_unival_subtrees(Node(1, Node(2)))[2] == 1

    def test_3(self):
        return count_unival_subtrees(Node(1, Node(1)))[2] == 2

    def test_4(self):
        return count_unival_subtrees(Node(1, None, Node(2)))[2] == 1

    def test_5(self):
        return count_unival_subtrees(Node(1, Node(1, Node(1), Node(1)), Node(1, None, Node(1))))[2] == 6

    def test_6(self):
        return count_unival_subtrees(Node(1, Node(1, Node(1), Node(2)), Node(1, None, Node(1))))[2] == 4

    def test_7(self):
        return count_unival_subtrees(Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))))[2] == 5

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

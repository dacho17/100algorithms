from FindSubtree import Node, find_subtree

class TestSuite:
    def test_1(self):
        return find_subtree(Node(1), Node(1)) == True

    def test_2(self):
        return find_subtree(Node(1, None, Node(2)), Node(2)) == True

    def test_3(self):
        return find_subtree(Node(1, None, Node(2)), Node(1)) == False

    def test_4(self):
        return find_subtree(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(4), Node(5))), Node(2, Node(4), Node(5))) == True

    def test_5(self):
        return find_subtree(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(4), Node(5))), Node(2, Node(5), Node(4))) == False

    def test_6(self):
        return find_subtree(Node(1, Node(2, Node(4, None, Node(6)), Node(5)), Node(3)), Node(4, None, Node(6))) == True

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

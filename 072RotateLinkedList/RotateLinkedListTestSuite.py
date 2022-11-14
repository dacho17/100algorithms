from RotateLinkedList import Node, rotate_list

class TestSuite:
    def test_1(self):
        return rotate_list(Node(1), 0) == "1"

    def test_2(self):
        return rotate_list(Node(1), 2) == "1"

    def test_3(self):
        return rotate_list(Node(1, Node(2, Node(3))), 1) == "312"

    def test_4(self):
        return rotate_list(Node(1, Node(2, Node(3))), 2) == "231"

    def test_5(self):
        return rotate_list(Node(1, Node(2, Node(3))), 6) == "123"

    def test_6(self):
        return rotate_list(Node(1, Node(2, Node(3, Node(4, Node(5))))), 2) == "45123"

    def test_7(self):
        return rotate_list(Node(1, Node(2)), 0) == "12"

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

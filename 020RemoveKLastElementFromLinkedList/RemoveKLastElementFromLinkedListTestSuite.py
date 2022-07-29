from RemoveKLastElementFromLinkedList import remove_from_end, Node

class TestSuite:
    def test_1(self):
        return str(remove_from_end(Node(1, Node(2, Node(3, Node(4, Node(5, None))))), 1)) == "[ 1, 2, 3, 4, ]"

    def test_2(self):
        return str(remove_from_end(Node(1, Node(2, Node(3, Node(4, Node(5, None))))), 5)) == "[ 2, 3, 4, 5, ]"

    def test_3(self):
        return str(remove_from_end(Node(1, Node(2, Node(3, Node(4, Node(5, None))))), 3)) == "[ 1, 2, 4, 5, ]"

    def test_4(self):
        return str(remove_from_end(Node(1, Node(2, None)), 2)) == "[ 2, ]"

    def test_5(self):
        return str(remove_from_end(Node(1, Node(2, None)), 1)) == "[ 1, ]"

    def test_6(self):
        return str(remove_from_end(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, None)))))), 6)) == "[ 2, 3, 4, 5, 6, ]"

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

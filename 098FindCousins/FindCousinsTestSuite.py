from FindCousins import Node, find_cousins

class TestSuite:
    def test_1(self):
        return find_cousins(Node(1), Node(1)) == [1]

    def test_2(self):
        return find_cousins(Node(1, None, Node(2)), Node(2)) == [2]

    def test_3(self):
        return find_cousins(Node(1, Node(2), Node(3)), Node(2)) == [2, 3]

    def test_4(self):
        return find_cousins(Node(1, Node(2, Node(3), Node(4)), Node(5, None, Node(6))), Node(2)) == [2, 5]

    def test_5(self):
        return find_cousins(Node(1, Node(2, Node(3, None, Node(11)), Node(4, Node(10))), Node(5, Node(15), Node(6, Node(12)))), Node(3)) == [3, 4, 15, 6]

    def test_6(self):
        return find_cousins(Node(0, Node(1, Node(11, Node(111), Node(112)), Node(12, Node(121), Node(122))), Node(2, Node(21, Node(211), Node(212)), Node(22, None, Node(222)))), Node(77)) == []

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

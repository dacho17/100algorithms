from RemoveZeroSumConsequtiveNodes import Node, remove_zero_sum_conseq

class TestSuite:
    def test_1(self):
        return str(remove_zero_sum_conseq(Node(1, None))) == "1 "

    def test_2(self):
        return str(remove_zero_sum_conseq(Node(2, Node(-2, None)))) == "None"

    def test_3(self):
        return str(remove_zero_sum_conseq(Node(0, Node(1, Node(0, Node(-1, Node(2, Node(1, Node(-3, Node(9, None)))))))))) == "9 "

    def test_4(self):
        return str(remove_zero_sum_conseq(Node(3, Node(1, Node(2, Node(-1, Node(2, Node(4, Node(1, None))))))))) == "3 1 2 -1 2 4 1 "

    def test_5(self):
        return str(remove_zero_sum_conseq(Node(3, Node(1, Node(-3, Node(2, None)))))) == "3 "

    def test_6(self):
        return str(remove_zero_sum_conseq(Node(3, Node(1, Node(-4, Node(2, None)))))) == "2 "

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

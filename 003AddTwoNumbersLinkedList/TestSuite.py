from AddTwoNumbers import Solution, Node

class AddTwoNumbersTestSuite:
    def __init__(self):
        self.sol = Solution()

    def test_1(self):
        digit1 = Node(2)
        digit1.next = Node(4)
        digit1.next.next = Node(3)
        digit2 = Node(5)
        digit2.next = Node(6)
        digit2.next.next = Node(4)
        sum = self.sol.add_func(digit1, digit2)
        sum_int = self.sol.transform_to_int(sum)
        return sum_int == 807
    # Expected: 807

    def test_2(self):
        digit1 = Node(2)
        digit1.next = Node(4)
        digit2 = Node(8)
        digit2.next = Node(5)
        digit2.next.next = Node(4)
        sum = self.sol.add_func(digit1, digit2)
        sum_int = self.sol.transform_to_int(sum)
        return sum_int == 500
    # Expected: 500

    def test_3(self):
        digit1 = Node(0)
        digit1.next = Node(1)
        digit1.next.next = Node(4)
        digit2 = Node(0)
        digit2.next = Node(0)
        digit2.next.next = Node(6)
        digit2.next.next.next = Node(7)
        sum = self.sol.add_func(digit1, digit2)
        sum_int = self.sol.transform_to_int(sum)
        return sum_int == 8010
    # Expected: 8010

    def test_4(self):
        digit1 = Node(0)
        digit2 = Node(8)
        digit2.next = Node(5)
        digit2.next.next = Node(8)
        sum = self.sol.add_func(digit1, digit2)
        sum_int = self.sol.transform_to_int(sum)
        return sum_int == 858
    # Expected: 858

    def test_5(self):
        digit1 = Node(0)
        digit2 = Node(0)
        sum = self.sol.add_func(digit1, digit2)
        sum_int = self.sol.transform_to_int(sum)
        return sum_int == 0
    # Expected: 0

    def test_6(self):
        digit1 = Node(9)
        digit1.next = Node(1)
        digit2 = Node(1)
        digit2.next = Node(8)
        digit1.next.next = Node(9)
        sum = self.sol.add_func(digit1, digit2)
        sum_int = self.sol.transform_to_int(sum)
        return sum_int == 1000
    # Expected: 1000
    
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

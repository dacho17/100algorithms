from SubarrayTargetSum import sliding_window, subArraySum

class TestSuite:
    def test_1(self):
        return subArraySum([5], 5) == [5]

    def test_2(self):
        return subArraySum([1, 2, 3], 6) == [1, 2, 3]

    def test_3(self):
        return subArraySum([4, 1, 3, 6], 10) == [1, 3, 6]

    def test_4(self):
        return subArraySum([1, 2, 3, 21, 5, 6, 7], 21) == [21]

    def test_5(self):
        return subArraySum([1, 3, 2, 5, 7, 2], 14) == [2, 5, 7]

    def test_6(self):
        return subArraySum([-4, 5, 7, 13, 20, 11, 9, -4, 10], 16) == [11, 9, -4]

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

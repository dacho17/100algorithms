from MaximumSubarraySum import get_max_sum

class TestSuite:
    def test_1(self):
        return get_max_sum([1, 0]) == 1

    def test_2(self):
        return get_max_sum([1, 0, - 1]) == 1

    def test_3(self):
        return get_max_sum([1, 0, 3, 2, -5, 6]) == 7

    def test_4(self):
        return get_max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_5(self):
        return get_max_sum([-3, -1, -3, -4, 1, 23, 1, -5, 5]) == 25

    def test_6(self):
        return get_max_sum([2, -1, 23, -3, -4, 5, 3, -5, 5]) == 25

    def test_7(self):
        return get_max_sum([-1, -1, -2, -3, -4, -5, -3, -5, -5]) == 0

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

from MinimumSubarrayLength import find_min_subarray_that_sums_to

class TestSuite:
    def test_1(self):
        return find_min_subarray_that_sums_to(1, [1]) == 1

    def test_2(self):
        return find_min_subarray_that_sums_to(2, [1, 1, 2, 1, 1]) == 1

    def test_3(self):
        return find_min_subarray_that_sums_to(5, [3, 2, 1, 3, 1, 2, 2]) == 2

    def test_4(self):
        return find_min_subarray_that_sums_to(7, [3, 2, 1, 7, 3, 4, 100, 2]) == 1

    def test_5(self):
        return find_min_subarray_that_sums_to(3, [1, 1, 1, 5, 1, 1, 4, 1, 1, 1]) == 3

    def test_6(self):
        return find_min_subarray_that_sums_to(25, [12, 45, 98, 13, 7, 4, 1, 16]) == 4

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

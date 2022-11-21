from LongestIncreasingSubsequence import longest_increasing_subsequence

class TestSuite:
    def test_1(self):
        return longest_increasing_subsequence([1]) == 1

    def test_2(self):
        return longest_increasing_subsequence([1, 2, 3]) == 3

    def test_3(self):
        return longest_increasing_subsequence([2, 1, 4, 5]) == 3

    def test_4(self):
        return longest_increasing_subsequence([2, 3, 0, 4, 12, -3, 25]) == 5

    def test_5(self):
        return longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3]) == 5

    def test_6(self):
        return longest_increasing_subsequence([10, -1, 7, -2, 4, -3, 3, -2]) == 2

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

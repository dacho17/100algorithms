from UniquePaths import unique_ways_DP

class TestSuite:
    def test_1(self):
        return unique_ways_DP(1, 3) == 1

    def test_2(self):
        return unique_ways_DP(10, 1) == 1

    def test_3(self):
        return unique_ways_DP(2, 2) == 2

    def test_4(self):
        return unique_ways_DP(7, 7) == 924

    def test_5(self):
        return unique_ways_DP(3, 5) == 15

    def test_6(self):
        return unique_ways_DP(5, 3) == 15

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

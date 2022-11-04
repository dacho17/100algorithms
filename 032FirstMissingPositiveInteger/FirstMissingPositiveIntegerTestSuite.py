from FirstMissingPositiveInteger import find_first_missing_positive

class TestSuite:
    def test_1(self):
        return find_first_missing_positive([0]) == 1

    def test_2(self):
        return find_first_missing_positive([1]) == None

    def test_3(self):
        return find_first_missing_positive([2]) == 1

    def test_4(self):
        return find_first_missing_positive([0, 1]) == 2

    def test_5(self):
        return find_first_missing_positive([0, 1, -1, 2, 3, -2, 5]) == 4

    def test_6(self):
        return find_first_missing_positive([3, 4, -1, 1]) == 2

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

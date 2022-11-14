from OptimizedArraySum import get_sum_quickly

class TestSuite:
    def test_1(self):
        return get_sum_quickly([1], 0, 0)

    def test_2(self):
        return get_sum_quickly([1, 2, 3], 0, 2) == 6

    def test_3(self):
        return get_sum_quickly([1, 2, 3], 1, 2) == 5
        
    def test_4(self):
        return get_sum_quickly([1, 2, 3, 4, 5, 6, 7], 3, 6) == 22

    def test_5(self):
        return get_sum_quickly([1, -5, 2, 9, 5, 3, 5], 0, 3) == 7

    def test_6(self):
        return get_sum_quickly([1, -5, 2, 9, 5, 3, 5], 1, 2) == -3

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

from FindKthLargestElement import findKthLargestQuickSelect

class TestSuite:
    def test_1(self):
        return findKthLargestQuickSelect([14, 2], 1) == 14

    def test_2(self):
        return findKthLargestQuickSelect([14, 2], 2) == 2

    def test_3(self):
        return findKthLargestQuickSelect([1, 3, 5, 7, 9, 11, 13], 3) == 9
    
    def test_4(self):
        return findKthLargestQuickSelect([13, 11, 9, 7, 3, -2], 6) == -2

    def test_5(self):
        return findKthLargestQuickSelect([5, 3, 8, 1, 9, 5, 2, 0, 4, 6, 7], 4) == 6

    def test_6(self):
        return findKthLargestQuickSelect([1, 2, 3, 9, 7, 5, 4], 3) == 5

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

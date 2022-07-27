from FindNonDuplicate import constant_find_non_duplicate, linear_find_non_duplicate

class TestSuite:
    def test_1(self):
        test_cons = constant_find_non_duplicate([4, 3, 2, 4, 1, 3, 2]) == 1
        test_lin = linear_find_non_duplicate([4, 3, 2, 4, 1, 3, 2]) == 1
        return test_cons and test_lin

    def test_2(self):
        test_cons = constant_find_non_duplicate([1, 1, 0, 0, 2, 3, 2]) == 3
        test_lin = linear_find_non_duplicate([1, 1, 0, 0, 2, 3, 2]) == 3
        return test_cons and test_lin

    def test_3(self):
        test_cons = constant_find_non_duplicate([10, 10, 12, 12, 7, 7, 2, 6, 2, 8, 8]) == 6
        test_lin = linear_find_non_duplicate([10, 10, 12, 12, 7, 7, 2, 6, 2, 8, 8]) == 6
        return test_cons and test_lin

    def test_4(self):
        test_cons = constant_find_non_duplicate([5, 2, 5, 0, 1, 0, 1]) == 2
        test_lin = linear_find_non_duplicate([5, 2, 5, 0, 1, 0, 1]) == 2
        return test_cons and test_lin

    def test_5(self):
        test_cons = constant_find_non_duplicate([4, 0, 4]) == 0
        test_lin = linear_find_non_duplicate([4, 0, 4]) == 0
        return test_cons and test_lin

    def test_6(self):
        test_cons = constant_find_non_duplicate([1, 1, 3, 2, 2]) == 3
        test_lin = linear_find_non_duplicate([1, 1, 3, 2, 2]) == 3
        return test_cons and test_lin
    
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

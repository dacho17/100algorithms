from FindFixedPoint import find_fixed_point

class TestSuite:
    def test_1(self):
        return find_fixed_point([1]) == None

    def test_2(self):
        return find_fixed_point([0]) == 0

    def test_3(self):
        return find_fixed_point([-1, 0, 2]) == 2

    def test_4(self):
        return find_fixed_point([0, 4, 7]) == 0

    def test_5(self):
        return find_fixed_point([-4, -2, 1, 3, 5, 6, 7, 8, 9, 10, 11, 12]) == 3

    def test_6(self):
        return find_fixed_point([-3, -2, -1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 12, 14, 15]) == 12

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

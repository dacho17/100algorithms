from ProductOfArrayExceptSelf import get_products

class TestSuite:
    def test_1(self):
        return get_products([1, 2, 3, 4]) == [24, 12, 8, 6]

    def test_2(self):
        return get_products([1, 2]) == [2, 1]

    def test_3(self):
        return get_products([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]

    def test_4(self):
        return get_products([7, 8, 6, 4, 5]) == [960, 840, 1120, 1680, 1344]

    def test_5(self):
        return get_products([1, 6, 0]) == [0, 0, 6]

    def test_6(self):
        return get_products([7, 3, 2, 1, 0, 0]) == [0, 0, 0, 0, 0, 0]

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

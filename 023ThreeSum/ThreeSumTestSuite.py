from ThreeSum import three_sum_pointers

class TestSuite:
    def test_1(self):
        return three_sum_pointers([-1, 0, 1, 2, -4, -3]) == [(-3, 1, 2), (-1, 0, 1)]
    def test_2(self):
        return three_sum_pointers([-1, 0, 1, 2, 3, 4, 5, -5, -3]) == [(-5, 0, 5), (-5, 1, 4), (-5, 2, 3), (-3, -1, 4), (-3, 0, 3), (-3, 1, 2), (-1, 0, 1)]

    def test_3(self):
        return three_sum_pointers([1, 4, -5, 0, -4, -1, 5]) == [(-5, 0, 5), (-5, 1, 4), (-4, -1, 5), (-4, 0, 4), (-1, 0, 1)]

    def test_4(self):
        return three_sum_pointers([1, 2, 0]) == []

    def test_5(self):
        return three_sum_pointers([1, 2, -3]) == [(-3, 1, 2)]

    def test_6(self):
        return three_sum_pointers([0, 1, -5]) == []

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

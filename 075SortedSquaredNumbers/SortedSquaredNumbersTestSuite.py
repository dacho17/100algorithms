from SortedSquaredNumbers import sorted_squares

class TestSuite:
    def test_1(self):
        return sorted_squares([0]) == [0]

    def test_2(self):
        return sorted_squares([0, 1, 2]) == [0, 1, 4]

    def test_3(self):
        return sorted_squares([-1, 0, 1]) == [0, 1, 1]

    def test_4(self):
        return sorted_squares([-3, -1, 1, 2, 4]) == [1, 1, 4, 9, 16]

    def test_5(self):
        return sorted_squares([-7, -5, -2, 0, 3, 5, 6]) == [0, 4, 9, 25, 25, 36, 49]

    def test_6(self):
        return sorted_squares([-6, -4, -3, -3, -1, 1, 3]) == [1, 1, 9, 9, 9, 16, 36]

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

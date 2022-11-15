from NumberAsSumOfSquares import as_sum_of_squares

class TestSuite:
    def test_1(self):
        return as_sum_of_squares(10) == 2

    def test_2(self):
        return as_sum_of_squares(5) == 2

    def test_3(self):
        return as_sum_of_squares(7) == 4

    def test_4(self):
        return as_sum_of_squares(75) == 3

    def test_5(self):
        return as_sum_of_squares(15) == 4

    def test_6(self):
        return as_sum_of_squares(1024) == 1

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

from SimpleCalculator import calculate

class TestSuite:
    def test_1(self):
        return calculate("1+(2+(3+(4+5)))") == 15
    # Expected: sum = 15

    def test_2(self):
        return calculate("1-(2+(3-(4+5)))") == 5
    # Expected: sum = 5

    def test_3(self):
        return calculate("(5+7)-((4+2-3)-6)") == 15
    # Expected: sum = 15

    def test_4(self):
        return calculate("(5+7)-(-(4+2-3)-6)") == 21
    # Expected: sum = 21

    def test_5(self):
        return calculate("(5+7)+(-(4+2-3)-6)") == 3
    # Expected: sum = 3

    def test_6(self):
        return calculate("-7+9-(4)-((-2+3)-4)") == 1
    # Expected: sum = 1

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

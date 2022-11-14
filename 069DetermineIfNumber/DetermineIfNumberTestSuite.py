from DetermineIfNumber import is_valid_number

class TestSuite:
    def test_1(self):
        return is_valid_number('123') == True

    def test_2(self):
        return is_valid_number('12.3') == True

    def test_3(self):
        return is_valid_number('-123') == True

    def test_4(self):
        return is_valid_number('-.3') == True

    def test_5(self):
        return is_valid_number('1.5e5') == True

    def test_6(self):
        return is_valid_number('12a') == False

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

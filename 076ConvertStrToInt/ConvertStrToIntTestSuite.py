from ConvertStrToInt import convert_str_to_int

class TestSuite:
    def test_1(self):
        return convert_str_to_int("0") == 0

    def test_2(self):
        return convert_str_to_int("4") == 4

    def test_3(self):
        return convert_str_to_int("10") == 10 

    def test_4(self):
        return convert_str_to_int("123497068") == 123497068

    def test_5(self):
        return convert_str_to_int("-679") == -679

    def test_6(self):
        return convert_str_to_int("-123084699307") == -123084699307

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

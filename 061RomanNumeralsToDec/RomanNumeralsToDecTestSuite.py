from RomanNumeralsToDec import transform_roman_dec

class TestSuite:
    def test_1(self):
        return transform_roman_dec("C") == 100

    def test_2(self):
        return transform_roman_dec("DCCVII") == 707

    def test_3(self):
        return transform_roman_dec("CLIX") == 159

    def test_4(self):
        return transform_roman_dec("DCCCLXXVII") == 877

    def test_5(self):
        return transform_roman_dec("CMXCIX") == 999

    def test_6(self):
        return transform_roman_dec("MCMXCV") == 1995

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

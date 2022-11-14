from MakeLargestNumber import build_largest_number

class TestSuite:
    def test_1(self):
        return build_largest_number([0]) == '0'

    def test_2(self):
        return build_largest_number([0, 2]) == '20'

    def test_3(self):
        return build_largest_number([2, 0, 23, 21]) == '232210'

    def test_4(self):
        return build_largest_number([17, 7, 72, 37, 6, 3]) == '772637317'

    def test_5(self):
        return build_largest_number([2, 223, 24, 22, 12, 29]) == '292422322212'

    def test_6(self):
        return build_largest_number([8, 83, 88, 889, 881, 832, 14, 6]) == '88988888183832614'

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

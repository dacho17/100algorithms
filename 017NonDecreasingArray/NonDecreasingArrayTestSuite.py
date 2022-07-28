from NonDecreasingArray import can_be_inclining

class TestSuite:
    def test_1(self):
        return can_be_inclining([2, 4]) == True

    def test_2(self):
        return can_be_inclining([4, 2]) == True

    def test_3(self):
        return can_be_inclining([4, 1, 2]) == True

    def test_4(self):
        return can_be_inclining([3, 2, 4, 1]) == False

    def test_5(self):
        return can_be_inclining([1, 5, 2, 3, 4]) == True

    def test_6(self):
        return can_be_inclining([1, 5, 2, 7, 4]) == False

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

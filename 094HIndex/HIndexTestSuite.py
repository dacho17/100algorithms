from HIndex import determine_h_index

class TestSuite:
    def test_1(self):
        return determine_h_index([0]) == 0

    def test_2(self):
        return determine_h_index([1]) == 1

    def test_3(self):
        return determine_h_index([4]) == 1

    def test_4(self):
        return determine_h_index([5, 3, 1, 0, 3]) == 3

    def test_5(self):
        return determine_h_index([7, 3, 5, 3, 5, 6]) == 4

    def test_6(self):
        return determine_h_index([4, 12, 8, 5, 9, 99, 12, 45, 10, 72]) == 8

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

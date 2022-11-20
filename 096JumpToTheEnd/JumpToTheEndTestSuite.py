from JumpToTheEnd import hop_to_end

class TestSuite:
    def test_1(self):
        return hop_to_end([1]) == 0

    def test_2(self):
        return hop_to_end([5]) == 0

    def test_3(self):
        return hop_to_end([1, 1]) == 1

    def test_4(self):
        return hop_to_end([3, 1]) == 1

    def test_5(self):
        return hop_to_end([3, 2, 5, 1, 1, 9, 3, 4]) == 2

    def test_6(self):
        return hop_to_end([1, 3, 2, 4, 7, 3, 5, 6, 7, 3, 1, 10]) == 3

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

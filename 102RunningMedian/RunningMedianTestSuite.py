from RunningMedian import get_sequence_medians

class TestSuite:
    def test_1(self):
        return get_sequence_medians([2]) == [2]

    def test_2(self):
        return get_sequence_medians([1, 2]) == [1, 1.5]

    def test_3(self):
        return get_sequence_medians([3, 5, 2, 7, 1, 9, 6]) == [3, 4, 3, 4, 3, 4, 5]

    def test_4(self):
        return get_sequence_medians([10, 5, 8, 3, 1, 15]) == [10, 7.5, 8, 6.5, 5, 6.5]

    def test_5(self):
        return get_sequence_medians([0, 0, 1, 1, 1, 0, 2, 1, 0]) == [0, 0, 0, 0.5, 1, 0.5, 1, 1, 1]

    def test_6(self):
        return get_sequence_medians([2, 1, 4, 7, 2, 0, 5]) == [2, 1.5, 2, 3, 2, 2, 2]

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

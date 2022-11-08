from MergeIntervals import get_intervals_from

class TestSuite:
    def test_1(self):
        return get_intervals_from([1, 2]) == [(1, 2)]

    def test_2(self):
        return get_intervals_from([1]) == [(1, 1)]

    def test_3(self):
        return get_intervals_from([1, 2, 4]) == [(1, 2), (4, 4)]

    def test_4(self):
        return get_intervals_from([1, 2, 4, 7, 8, 9]) == [(1, 2), (4, 4), (7, 9)]

    def test_5(self):
        return get_intervals_from([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]) == [(0, 2), (5, 5), (7, 11), (15, 15)]

    def test_6(self):
        return get_intervals_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 11, 11, 12, 13, 13, 15, 15, 16, 16, 17]) == [(1, 13), (15, 17)]

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

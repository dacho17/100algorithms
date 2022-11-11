from MergeIntervals import merge_intervals

class TestSuite:
    def test_1(self):
        return merge_intervals([(0, 5)]) == [(0, 5)]

    def test_2(self):
        return merge_intervals([(0, 2), (3, 4)]) == [(0, 2), (3, 4)]

    def test_3(self):
        return merge_intervals([(1, 6), (2, 4)]) == [(1, 6)]

    def test_4(self):
        return merge_intervals([(1, 4), (4, 7)]) == [(1, 7)]

    def test_5(self):
        return merge_intervals([(1, 5), (7, 12), (12, 12), (7, 7), (10, 10), (10, 11), (8, 11), (8, 10), (14, 20)]) == [(1, 5), (7, 12), (14, 20)]

    def test_6(self):
        return merge_intervals([(1, 5), (14, 20), (8, 10), (7, 14)]) == [(1, 5), (7, 20)]

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

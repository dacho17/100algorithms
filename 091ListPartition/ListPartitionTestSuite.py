from ListPartition import partition

class TestSuite:
    def test_1(self):
        return partition([1], 2) == [1]

    def test_2(self):
        return partition([1, 5, 2], 3) == [1, 2, 5]

    def test_3(self):
        return partition([10, -7, 4, 13, 2, 12, 1, 0, 17], 5) == [0, -7, 4, 1, 2, 12, 13, 17, 10]

    def test_4(self):
        return partition([8, 9, 2, 4, 1, 0], 3) == [0, 1, 2, 4, 9, 8]

    def test_5(self):
        return partition([7, 3, -4, 5, -2, 0, 0, 1, -2, 0, 16, -7, 3, 0, 1, 5], 0) == [-7, -4, -2, -2, 0, 0, 0, 0, 1, 16, 5, 3, 3, 1, 5, 7]

    def test_6(self):
        return partition([-5, 0, 3, 0, -2, 0, 1, 4], 0) == [-5, -2, 0, 0, 0, 1, 4, 3]

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

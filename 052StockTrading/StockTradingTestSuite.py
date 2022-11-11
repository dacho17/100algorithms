from StockTrading import find_best_trade, find_min_max

class TestSuite:
    def test_1(self):
        return find_best_trade([1, 1]) == 0

    def test_2(self):
        return find_best_trade([1, 2, 3, 4]) == 3

    def test_3(self):
        return find_best_trade([1, 3, 5, 3, 4, 6, 2, 5, 0]) == 5

    def test_4(self):
        return find_best_trade([7, 4, 0, 1, 3, 5, 3, 4, 6, 2, 5, 0]) == 6

    def test_5(self):
        return find_best_trade([9, 11, 8, 5, 7, 10]) == 5

    def test_6(self):
        return find_best_trade([1, 3, 5, 7, 9, 2, 9, 0, 9, 1, 5]) == 9

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

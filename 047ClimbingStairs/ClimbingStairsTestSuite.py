from ClimbingStairs import climbing_combinations, fibonacci

class TestSuite:
    def test_1(self):
        return fibonacci(1) == climbing_combinations(1) == 1

    def test_2(self):
        return fibonacci(2) == climbing_combinations(2) == 2

    def test_3(self):
        return fibonacci(3) == climbing_combinations(3) == 3

    def test_4(self):
        return fibonacci(4) == climbing_combinations(4) == 5

    def test_5(self):
        return fibonacci(5) == climbing_combinations(5) == 8

    def test_6(self):
        return fibonacci(7) == climbing_combinations(7) == 21

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

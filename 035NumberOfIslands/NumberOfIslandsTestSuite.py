from NumberOfIslands import count_number_of_islands

class TestSuite:
    def test_1(self):
        return count_number_of_islands([[1]]) == 1

    def test_2(self):
        return count_number_of_islands([[0]]) == 0

    def test_3(self):
        return count_number_of_islands([[1, 0], [0, 1]]) == 2

    def test_4(self):
        return count_number_of_islands([[1, 0], [1, 0]]) == 1

    def test_5(self):
        return count_number_of_islands([[1, 0, 1], [0, 1, 0], [1, 0, 1]]) == 5

    def test_6(self):
        return count_number_of_islands([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) == 4

    def test_7(self):
        return count_number_of_islands([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]) == 8

    def test_8(self):
        return count_number_of_islands([[1, 1, 1], [0, 1, 0], [1, 1, 1]]) == 1

    def test_9(self):
        return count_number_of_islands([[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0]])

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
        print("Test_7 : " + self.return_test_result(self.test_7))
        print("Test_8 : " + self.return_test_result(self.test_8))
        print("Test_9 : " + self.return_test_result(self.test_9))
        print("Test suite finished running")

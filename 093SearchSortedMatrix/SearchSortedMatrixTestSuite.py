from SearchSortedMatrix import binary_search_matrix

class TestSuite:
    def test_1(self):
        return binary_search_matrix([[1]], 1) == True

    def test_2(self):
        return binary_search_matrix([[1]], 2) == False

    def test_3(self):
        return binary_search_matrix([[1, 2], [3, 4]], 3) == True

    def test_4(self):
        return binary_search_matrix([[1, 2], [3, 4]], 2) == True

    def test_5(self):
        return binary_search_matrix([[1, 2], [3, 4]], 1) == True

    def test_6(self):
        return binary_search_matrix([[1, 2], [3, 4]], 4) == True

    def test_7(self):
        return binary_search_matrix([[1, 2], [3, 4]], 7) == False

    def test_8(self):
        return binary_search_matrix([[1, 2], [3, 4]], 0) == False

    def test_9(self):
        return binary_search_matrix([[1, 3, 5, 8],
                                    [10, 11, 15, 16],
                                    [24, 27, 30, 31]], 10) == True
    def test_10(self):
        return binary_search_matrix([[1, 3, 5, 8],
                                    [10, 11, 15, 16],
                                    [24, 27, 30, 31]], 4) == False

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
        print("Test_10 : " + self.return_test_result(self.test_10))
        print("Test suite finished running")

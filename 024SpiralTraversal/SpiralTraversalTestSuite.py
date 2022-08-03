from SpiralTraversal import Grid

class TestSuite:
    def test_1(self):
        return Grid([[0]]).traverse_spirally() == [0]

    def test_2(self):
        return Grid([[1, 2, 3]]).traverse_spirally() == [1, 2, 3]

    def test_3(self):
        return Grid([[1], [2]]).traverse_spirally() == [1, 2]

    def test_4(self):
        return Grid([[1, 2, 3, 4], [5, 6, 7, 8]]).traverse_spirally() == [1, 2, 3, 4, 8, 7, 6, 5]

    def test_5(self):
        return Grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).traverse_spirally() == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    def test_6(self):
        return Grid([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]).traverse_spirally() == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
    
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

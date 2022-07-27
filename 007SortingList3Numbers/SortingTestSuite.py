from Sorting3Nums import two_pointer_sort

class TestSuite:
    def test_1(self):
        return two_pointer_sort([3, 1, 2, 2, 3, 1, 2], 1, 3) == [1, 1, 2, 2, 2, 3, 3]

    def test_2(self):
        return two_pointer_sort([2, 1, 3, 2, 2, 1, 3], 1, 3) == [1, 1, 2, 2, 2, 3, 3]

    def test_3(self):
        return two_pointer_sort([3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1], 1, 3) == [1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3]

    def test_4(self):
        return two_pointer_sort([7, 8, 9], 7, 9) == [7, 8, 9]

    def test_5(self):
        return two_pointer_sort([9, 8, 7], 7, 9) == [7, 8, 9]

    def test_6(self):
        return two_pointer_sort([0, 1, 5, 0, 1, 5, 1, 5, 0, 0, 1], 0, 5) == [0, 0, 0, 0, 1, 1, 1, 1, 5, 5, 5]
    
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

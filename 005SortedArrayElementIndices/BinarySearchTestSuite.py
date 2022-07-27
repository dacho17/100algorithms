from BinarySearch import ListForBinarySearch

class TestSuite:
    def test_1(self):
        lo, hi =  ListForBinarySearch([1, 3, 3, 5, 7, 8, 9, 9, 15]).get_occurence_range_for(9)
        return lo == 6 and hi == 7
    # Expected: range is [6, 7]

    def test_2(self):
        lo, hi =  ListForBinarySearch([1, 3, 3, 5, 7, 8, 9, 9, 15]).get_occurence_range_for(3)
        return lo == 1 and hi == 2
    # Expected: range is [1, 2]

    def test_3(self):
        lo, hi =  ListForBinarySearch([1, 3, 3, 5, 7, 8, 9, 9, 15]).get_occurence_range_for(15)
        return lo == 8 and hi == 8
    # Expected: range is [8]

    def test_4(self):
        lo, hi =  ListForBinarySearch([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 9, 9, 15]).get_occurence_range_for(3)
        return lo == 1 and hi == 12
    # Expected: range is [1, 12]

    def test_5(self):
        lo, hi =  ListForBinarySearch([0]).get_occurence_range_for(0)
        return lo == 0 and hi == 0
    # Expected: range is [0, 0]

    def test_6(self):
        lo, hi =  ListForBinarySearch([1] * 126).get_occurence_range_for(1)
        return lo == 0 and hi == 125
    # Expected: range is [0, 125]
    
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

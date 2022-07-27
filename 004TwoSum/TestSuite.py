from TwoSum import Numbers

class TwoSumTestSuite:
    def test_1(self):
        (add1, add2) = Numbers([2, 7, 11, 15]).get_addends_indices_for(18)
        return add1 == 1 and add2 == 2
    # Expected: addend_indices = (1, 2)

    def test_2(self):
        (add1, add2) = Numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).get_addends_indices_for(1)
        return add1 == 0 and add2 == 1
    # Expected: addend_indices = (0, 1)

    def test_3(self):
        (add1, add2) = Numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).get_addends_indices_for(9)
        return add1 == 4 and add2 == 5
    # Expected: addend_indices = (4, 5)

    def test_4(self):
        (add1, add2) = Numbers([1, 2, 3, 4]).get_addends_indices_for(8)
        return add1 == None and add2 == None
    # Expected: addend_indices = (None, None)

    def test_5(self):
        (add1, add2) = Numbers([0, 1, 2, 3, 4, 5, 10]).get_addends_indices_for(10)
        return add1 == 0 and add2 == 6
    # Expected: addend_indices = (0, 6)

    def test_6(self):
        (add1, add2) = Numbers([0, 1, 2, 3, 4, 5, 10]).get_addends_indices_for(6)
        return add1 == 2 and add2 == 4
    # Expected: addend_indices = (2, 4)
    
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

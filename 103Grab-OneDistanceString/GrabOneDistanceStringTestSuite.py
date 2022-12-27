from GrabOneDistanceString import is_one_edit_distance

class TestSuite:
    def test_1(self):
        return is_one_edit_distance("fog", "foo") == True
    
    def test_2(self):
        return is_one_edit_distance("fog", "fo") == True
    
    def test_3(self):
        return is_one_edit_distance("grab", "grab") == False
    
    def test_4(self):
        return is_one_edit_distance("grab", "brag") == False
    
    def test_5(self):
        return is_one_edit_distance("", "ab") == False

    def test_6(self):
        return is_one_edit_distance("abqde", "abde") == True

    def test_7(self):
        return is_one_edit_distance("abqde", "bqde") == True

    def test_8(self):
        return is_one_edit_distance("abqde", "abqd") == True
        
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
        print("Test suite finished running")
